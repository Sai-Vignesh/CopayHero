import os
import json
from bs4 import BeautifulSoup

# Directories
FILES_DIR = "./html_files/"
OUTPUT_JSON_FILE = "combined_drug_data.json"

# Function to extract drug data from a single HTML file
def extract_drug_data_from_html(file_path):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        pharmacies = []

        # Locate the section containing price information for pharmacies
        loc_list = soup.find('div', {'id': 'loc-list'})
        if not loc_list:
            return pharmacies

        pharmacy_items = loc_list.find_all('div', class_='pharmacy-item__details')
        for item in pharmacy_items:
            pharmacy_name_tag = item.find('div', class_='pharmcy-item-image')
            pharmacy_price_tag = item.find('div', class_='pharmacy-item__price')

            if pharmacy_name_tag and pharmacy_price_tag:
                # Extract pharmacy name
                pharmacy_name_img = pharmacy_name_tag.find('img')
                pharmacy_name = pharmacy_name_img.get('data-name', '').split(' at ')[-1] if pharmacy_name_img else "Unknown"

                # Extract price
                pharmacy_price = pharmacy_price_tag.get_text(strip=True)

                # Append data to the list
                pharmacies.append({
                    "pharmacy_name": pharmacy_name,
                    "price": pharmacy_price
                })

        return pharmacies

# Iterate over all HTML files and extract data into a single list
def extract_data_from_all_files():
    all_drug_data = []
    
    # Loop through all HTML files in the directory
    for file in sorted(os.listdir(FILES_DIR)):
        if file.endswith('.html'):
            file_path = os.path.join(FILES_DIR, file)
            pharmacies_data = extract_drug_data_from_html(file_path)
            
            # Add the pharmacies data to the final list
            if pharmacies_data:
                all_drug_data.append({
                    "file_name": file,  # Keep track of which file the data came from
                    "pharmacies": pharmacies_data
                })

    return all_drug_data

# Save the extracted data into a JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data has been saved to {output_file}")

# Main function to execute the workflow
def main():
    # Extract data from all HTML files
    drug_data = extract_data_from_all_files()

    # Save the combined data to a single JSON file
    save_to_json(drug_data, OUTPUT_JSON_FILE)

if __name__ == "__main__":
    main()
