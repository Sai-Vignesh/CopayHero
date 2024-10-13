from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from datetime import datetime
import numpy as np
import openai
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate with app and db


# Load OpenAI API key
load_dotenv()
client = openai
client.api_key = os.environ["OPENAI_API_KEY"]


# Load embeddings store
with open('embeddings_store.json', 'r') as f:
    embeddings_store = json.load(f)

# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# Function to find the most similar embedding
def find_most_similar(query_embedding, embeddings_store, top_n=1):
    similarities = []
    for item in embeddings_store:
        similarity = cosine_similarity(query_embedding, item['embedding'])
        similarities.append((item['text'], similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

# Function to answer user questions
def answer_question(query):
    query_embedding = client.embeddings.create(input=query, model="text-embedding-ada-002")['data'][0]['embedding']
    most_similar = find_most_similar(query_embedding, embeddings_store)
    return most_similar[0][0] if most_similar else "No relevant answer found."

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))  # Redirect logged-in users away from register page

    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Validate password confirmation
        if password != confirm_password:
            return "Passwords do not match!"

        # Save the user data to the database
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Log the user in after registration
        session['user_id'] = new_user.id
        session['user_first_name'] = new_user.first_name
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))  # Redirect logged-in users away from login page

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the database for a user with this email
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            # Store user details in session
            session['user_id'] = user.id
            session['user_first_name'] = user.first_name
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear session data
    session.pop('user_id', None)
    session.pop('user_first_name', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/discussion_board', methods=['GET', 'POST'])
def discussion_board():
    if request.method == 'POST':
        content = request.form['content']
        user_id = session.get('user_id')
        
        if user_id:
            # If user is logged in, associate post with the user
            new_post = Post(content=content, user_id=user_id)
        else:
            # Create a post with an anonymous user
            anonymous_user = User.query.filter_by(first_name="Anonymous").first()
            if not anonymous_user:
                # If the anonymous user does not exist, create one
                anonymous_user = User(first_name="Anonymous", last_name="", email="anonymous@copayhero.com", password="")
                db.session.add(anonymous_user)
                db.session.commit()
            new_post = Post(content=content, user_id=anonymous_user.id)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('discussion_board'))

    # Fetch all posts to display
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('discussion_board.html', posts=posts)

@app.route('/user_page/<int:user_id>')
def user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_page.html', user=user)

@app.route('/chat_now', methods=['GET', 'POST'])
def chat_now():
    answer = None
    if request.method == 'POST':
        question = request.form['question']
        answer = answer_question(question)
    return render_template('chatnow.html', answer=answer)



if __name__ == '__main__':
    app.run(debug=True)
