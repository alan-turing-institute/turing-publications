import json
import csv
import os

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_data(json_data):
    extracted_data = []
    for entry in json_data:
        titles = ', '.join([title.get('title', 'N/A') for title in entry.get('attributes', {}).get('titles', [])])
        creators = ', '.join([creator.get('name', 'N/A') for creator in entry.get('attributes', {}).get('creators', [])])
        doi = entry.get('attributes', {}).get('doi', 'N/A')
        publisher = entry.get('attributes', {}).get('publisher', 'N/A')
        year_published = entry.get('attributes', {}).get('publicationYear', 'N/A')
        
        extracted_data.append([titles, creators, doi, publisher, year_published])
    return extracted_data

def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Creators', 'DOI', 'Publisher', 'Year Published'])
        writer.writerows(data)

if __name__ == "__main__":
    json_file_path = os.path.join("..", "data", "datacite_response_data.json")  # Adjust the path as needed
    csv_file_path = os.path.join("..", "data", "datacite_extracted_data.csv")  #

    json_data = load_json_data(json_file_path)
    extracted_data = extract_data(json_data)
    save_to_csv(extracted_data, csv_file_path)