# # # import os
# # # import json
# # # from dotenv import load_dotenv
# # # load_dotenv()

# # # from openai import OpenAI
# # # from bs4 import BeautifulSoup

# # # # Load OpenAI API key
# # # client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# # # FILES_DIR = "./html_files/"
# # # JSON_DIR = "./json_files/"

# # # # Create directory for JSON files if it doesn't exist
# # # if not os.path.exists(JSON_DIR):
# # #     os.makedirs(JSON_DIR)

# # # # Function to extract drug data from HTML file and convert it to JSON
# # # def extract_drug_data_from_html(file_path):
# # #     print(file_path)
# # #     with open(file_path, 'r', encoding='utf-8') as file:
# # #         soup = BeautifulSoup(file, 'html.parser')
# # #         pharmacies = []

# # #         # Locate the section containing price information for pharmacies
# # #         loc_list = soup.find('div', {'id': 'loc-list'})
# # #         if not loc_list:
# # #             return pharmacies

# # #         pharmacy_items = loc_list.find_all(
# # #             'div', class_='pharmacy-item__details')
# # #         print(len(pharmacy_items))
# # #         for item in pharmacy_items:
# # #             pharmacy_name_tag = item.find('div', class_='pharmcy-item-image')
# # #             pharmacy_price_tag = item.find('div', class_='pharmacy-item__price')

# # #             if pharmacy_name_tag and pharmacy_price_tag:
# # #                 # Extract pharmacy name
# # #                 pharmacy_name = pharmacy_name_tag.img.get('data-name', '').split(' at ')[-1]
# # #                 # print(pharmacy_name)

# # #                 # Extract price
# # #                 pharmacy_price = pharmacy_price_tag.get_text(strip=True)
# # #                 # print(pharmacy_price)

# # #                 # Append data
# # #                 pharmacies.append({
# # #                     "pharmacy_name": pharmacy_name,
# # #                     "price": pharmacy_price
# # #                 })

# # #         return pharmacies

# # # # Iterate over each HTML file in the specified directory
# # # for file in sorted(os.listdir(FILES_DIR)):
# # #     if file.endswith('.html'):
# # #         file_path = os.path.join(FILES_DIR, file)
# # #         drug_data = extract_drug_data_from_html(file_path)

# # #         # Create JSON file for each HTML file
# # #         json_file_path = os.path.join(JSON_DIR, f"{os.path.splitext(file)[0]}.json")
# # #         with open(json_file_path, 'w', encoding='utf-8') as json_file:
# # #             json.dump(drug_data, json_file, indent=4)

# # #         print(f"Converted {file} to JSON and saved as {json_file_path}")

# # # # Function to create embeddings from JSON data
# # # def create_embeddings_from_json(json_file_path):
# # #     with open(json_file_path, 'r', encoding='utf-8') as json_file:
# # #         drug_data = json.load(json_file)
        
# # #         # Convert drug data to a text format suitable for embeddings
# # #         drug_texts = []
# # #         for drug in drug_data:
# # #             drug_name = drug["drug_name"]
# # #             pharmacies = ", ".join([f"{p['pharmacy_name']}: {p['price']}" for p in drug["pharmacies"]])
# # #             drug_text = f"Drug: {drug_name}\nPharmacies: {pharmacies}"
# # #             drug_texts.append(drug_text)

# # #         # Use OpenAI API to create embeddings for each drug's information
# # #         embeddings = []
# # #         for text in drug_texts:
# # #             response = client.embeddings.create(input=text, model="text-embedding-ada-002")
# # #             embeddings.append(response["data"][0]["embedding"])

# # #         return embeddings

# # # # Create embeddings for each JSON file
# # # for file in sorted(os.listdir(JSON_DIR)):
# # #     if file.endswith('.json'):
# # #         json_file_path = os.path.join(JSON_DIR, file)
# # #         embeddings = create_embeddings_from_json(json_file_path)
# # #         print(f"Created embeddings for {file}")

# # # print("All HTML files have been converted to JSON and embeddings have been created.")


# # import os
# # import json
# # from dotenv import load_dotenv
# # load_dotenv()

# # from openai import OpenAI
# # from bs4 import BeautifulSoup

# # # Load OpenAI API key
# # client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# # FILES_DIR = "./html_files/"
# # JSON_DIR = "./json_files/"

# # # Create directory for JSON files if it doesn't exist
# # if not os.path.exists(JSON_DIR):
# #     os.makedirs(JSON_DIR)

# # # Function to extract drug data from HTML file and convert it to JSON
# # def extract_drug_data_from_html(file_path):
# #     print(file_path)
# #     with open(file_path, 'r', encoding='utf-8') as file:
# #         soup = BeautifulSoup(file, 'html.parser')
# #         pharmacies = []

# #         # Locate the section containing price information for pharmacies
# #         loc_list = soup.find('div', {'id': 'loc-list'})
# #         if not loc_list:
# #             return pharmacies

# #         pharmacy_items = loc_list.find_all('div', class_='pharmacy-item__details')
# #         print(len(pharmacy_items))
# #         for item in pharmacy_items:
# #             pharmacy_name_tag = item.find('div', class_='pharmcy-item-image')
# #             pharmacy_price_tag = item.find('div', class_='pharmacy-item__price')

# #             if pharmacy_name_tag and pharmacy_price_tag:
# #                 # Extract pharmacy name
# #                 pharmacy_name_img = pharmacy_name_tag.find('img')
# #                 if pharmacy_name_img and pharmacy_name_img.has_attr('data-name'):
# #                     pharmacy_name = pharmacy_name_img.get('data-name', '').split(' at ')[-1]
# #                 else:
# #                     pharmacy_name = "Unknown"

# #                 # Extract price
# #                 pharmacy_price = pharmacy_price_tag.get_text(strip=True)

# #                 # Append data
# #                 pharmacies.append({
# #                     "pharmacy_name": pharmacy_name,
# #                     "price": pharmacy_price
# #                 })

# #         return pharmacies

# # # Iterate over each HTML file in the specified directory
# # for file in sorted(os.listdir(FILES_DIR)):
# #     if file.endswith('.html'):
# #         file_path = os.path.join(FILES_DIR, file)
# #         drug_data = extract_drug_data_from_html(file_path)

# #         # Create JSON file for each HTML file
# #         json_file_path = os.path.join(JSON_DIR, f"{os.path.splitext(file)[0]}.json")
# #         with open(json_file_path, 'w', encoding='utf-8') as json_file:
# #             json.dump(drug_data, json_file, indent=4)

# #         print(f"Converted {file} to JSON and saved as {json_file_path}")

# # # Function to create embeddings from JSON data
# # def create_embeddings_from_json(json_file_path):
# #     with open(json_file_path, 'r', encoding='utf-8') as json_file:
# #         drug_data = json.load(json_file)
        
# #         # Convert drug data to a text format suitable for embeddings
# #         drug_texts = []
# #         for drug in drug_data:
# #             drug_name = drug.get("drug_name", "Unknown Drug")
# #             pharmacies = ", ".join([f"{p['pharmacy_name']}: {p['price']}" for p in drug.get("pharmacies", [])])
# #             drug_text = f"Drug: {drug_name}\nPharmacies: {pharmacies}"
# #             drug_texts.append(drug_text)

# #         # Use OpenAI API to create embeddings for each drug's information
# #         embeddings = []
# #         for text in drug_texts:
# #             response = client.embeddings.create(input=text, model="text-embedding-ada-002")
# #             embeddings.append(response["data"][0]["embedding"])

# #         return embeddings

# # # Create embeddings for each JSON file
# # for file in sorted(os.listdir(JSON_DIR)):
# #     if file.endswith('.json'):
# #         json_file_path = os.path.join(JSON_DIR, file)
# #         embeddings = create_embeddings_from_json(json_file_path)
# #         print(f"Created embeddings for {file}")

# # print("All HTML files have been converted to JSON and embeddings have been created.")

# import os
# import json
# import time
# import numpy as np
# from dotenv import load_dotenv
# from bs4 import BeautifulSoup
# import openai

# # Load OpenAI API key
# load_dotenv()
# client = openai
# client.api_key = os.environ["OPENAI_API_KEY"]

# FILES_DIR = "./html_files/"
# JSON_DIR = "./json_files/"

# # Create directory for JSON files if it doesn't exist
# if not os.path.exists(JSON_DIR):
#     os.makedirs(JSON_DIR)

# # Function to extract drug data from HTML file and convert it to JSON
# def extract_drug_data_from_html(file_path):
#     print(f"Processing file: {file_path}")
#     with open(file_path, 'r', encoding='utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')
#         pharmacies = []

#         # Locate the section containing price information for pharmacies
#         loc_list = soup.find('div', {'id': 'loc-list'})
#         if not loc_list:
#             return pharmacies

#         pharmacy_items = loc_list.find_all('div', class_='pharmacy-item__details')
#         for item in pharmacy_items:
#             pharmacy_name_tag = item.find('div', class_='pharmcy-item-image')
#             pharmacy_price_tag = item.find('div', class_='pharmacy-item__price')

#             if pharmacy_name_tag and pharmacy_price_tag:
#                 # Extract pharmacy name
#                 pharmacy_name_img = pharmacy_name_tag.find('img')
#                 pharmacy_name = pharmacy_name_img.get('data-name', '').split(' at ')[-1] if pharmacy_name_img else "Unknown"

#                 # Extract price
#                 pharmacy_price = pharmacy_price_tag.get_text(strip=True)

#                 # Append data
#                 pharmacies.append({
#                     "pharmacy_name": pharmacy_name,
#                     "price": pharmacy_price
#                 })

#         return pharmacies

# # Step 1: Extract data from HTML and store embeddings

# # Store embeddings along with text
# embeddings_store = []

# # Iterate over each HTML file in the specified directory and convert to JSON
# for file in sorted(os.listdir(FILES_DIR)):
#     if file.endswith('.html'):
#         file_path = os.path.join(FILES_DIR, file)
#         drug_data = extract_drug_data_from_html(file_path)

#         # Save extracted data to JSON
#         json_file_path = os.path.join(JSON_DIR, f"{os.path.splitext(file)[0]}.json")
#         with open(json_file_path, 'w', encoding='utf-8') as json_file:
#             json.dump(drug_data, json_file, indent=4)

#         print(f"Converted {file} to JSON and saved as {json_file_path}")

#         # Generate embeddings for the data and store them
#         for drug in drug_data:
#             pharmacies = ", ".join([f"{p['pharmacy_name']}: {p['price']}" for p in drug.get("pharmacies", [])])
#             drug_text = f"Pharmacies: {pharmacies}"

#             # Generate embedding for the drug text
#             embedding = client.embeddings.create(input=drug_text, model="text-embedding-ada-002")['data'][0]['embedding']

#             # Store the embedding and text
#             embeddings_store.append({
#                 "text": drug_text,
#                 "embedding": embedding
#             })

# # Save the embeddings store to a file for later retrieval
# with open('embeddings_store.json', 'w') as f:
#     json.dump(embeddings_store, f)

# print("Embeddings have been stored successfully.")

# # Step 2: Cosine similarity function to find similar embeddings
# def cosine_similarity(vec1, vec2):
#     dot_product = np.dot(vec1, vec2)
#     norm_vec1 = np.linalg.norm(vec1)
#     norm_vec2 = np.linalg.norm(vec2)
#     return dot_product / (norm_vec1 * norm_vec2)

# # Function to find the most similar embedding
# def find_most_similar(query_embedding, embeddings_store, top_n=1):
#     similarities = []

#     for item in embeddings_store:
#         similarity = cosine_similarity(query_embedding, item['embedding'])
#         similarities.append((item['text'], similarity))

#     # Sort by similarity (highest first)
#     similarities.sort(key=lambda x: x[1], reverse=True)
    
#     # Return the top N most similar texts
#     return similarities[:top_n]

# # Step 3: Answer questions based on embeddings

# # Function to answer user queries
# def answer_question(query):
#     # Create embedding for the user query
#     query_embedding = client.embeddings.create(input=query, model="text-embedding-ada-002")['data'][0]['embedding']
    
#     # Load stored embeddings
#     with open('embeddings_store.json', 'r') as f:
#         embeddings_store = json.load(f)

#     # Find the most similar stored embedding
#     most_similar = find_most_similar(query_embedding, embeddings_store)
    
#     # Return the text corresponding to the most similar embedding
#     return most_similar[0][0] if most_similar else "No relevant answer found."

# # Example usage:
# user_query = "What is the price of Humira?"
# answer = answer_question(user_query)
# print("Answer:", answer)

import os
import json
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from bs4 import BeautifulSoup

# Load OpenAI API key
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

FILES_DIR = "./html_files/"
JSON_DIR = "./json_files/"
EMBEDDINGS_FILE = "embeddings_store.json"

# Create directory for JSON files if it doesn't exist
if not os.path.exists(JSON_DIR):
    os.makedirs(JSON_DIR)

# Function to extract drug data from HTML file and convert it to JSON
def extract_drug_data_from_html(file_path):
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        pharmacies = []

        # Locate the section containing price information for pharmacies
        loc_list = soup.find('div', {'id': 'loc-list'})
        if not loc_list:
            return pharmacies

        pharmacy_items = loc_list.find_all(
            'div', class_='pharmacy-item__details')
        print(len(pharmacy_items))
        for item in pharmacy_items:
            pharmacy_name_tag = item.find('div', class_='pharmcy-item-image')
            pharmacy_price_tag = item.find('div', class_='pharmacy-item__price')

            if pharmacy_name_tag and pharmacy_price_tag:
                # Extract pharmacy name
                pharmacy_name_img = pharmacy_name_tag.find('img')
                if pharmacy_name_img and pharmacy_name_img.has_attr('data-name'):
                    pharmacy_name = pharmacy_name_img.get('data-name', '').split(' at ')[-1]
                else:
                    pharmacy_name = "Unknown"

                # Extract price
                pharmacy_price = pharmacy_price_tag.get_text(strip=True)

                # Append data
                pharmacies.append({
                    "pharmacy_name": pharmacy_name,
                    "price": pharmacy_price
                })

        return pharmacies

# Iterate over each HTML file in the specified directory
for file in sorted(os.listdir(FILES_DIR)):
    if file.endswith('.html'):
        file_path = os.path.join(FILES_DIR, file)
        drug_data = extract_drug_data_from_html(file_path)

        # Create JSON file for each HTML file
        json_file_path = os.path.join(JSON_DIR, f"{os.path.splitext(file)[0]}.json")
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(drug_data, json_file, indent=4)

        print(f"Converted {file} to JSON and saved as {json_file_path}")

# Function to create embeddings from JSON data
def create_embeddings_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        drug_data = json.load(json_file)
        
        # Convert drug data to a text format suitable for embeddings
        drug_texts = []
        for drug in drug_data:
            drug_name = drug.get("drug_name", "Unknown Drug")
            pharmacies = ", ".join([f"{p['pharmacy_name']}: {p['price']}" for p in drug.get("pharmacies", [])])
            drug_text = f"Drug: {drug_name}\nPharmacies: {pharmacies}"
            drug_texts.append(drug_text)

        # Use OpenAI API to create embeddings for each drug's information
        embeddings = []
        for text in drug_texts:
            response = client.embeddings.create(input=text, model="text-embedding-ada-002")
            embeddings.append(response["data"][0]["embedding"])

        return embeddings

# Create embeddings for each JSON file and save to a combined JSON file
all_embeddings = {}
for file in sorted(os.listdir(JSON_DIR)):
    if file.endswith('.json'):
        json_file_path = os.path.join(JSON_DIR, file)
        embeddings = create_embeddings_from_json(json_file_path)
        all_embeddings[file] = embeddings
        print(f"Created embeddings for {file}")

# Save all embeddings to a JSON file
with open(EMBEDDINGS_FILE, 'w', encoding='utf-8') as embeddings_file:
    json.dump(all_embeddings, embeddings_file, indent=4)

print(f"All embeddings have been saved to {EMBEDDINGS_FILE}")
print("All HTML files have been converted to JSON and embeddings have been created.")