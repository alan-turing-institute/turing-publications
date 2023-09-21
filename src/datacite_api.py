import requests
import json
import os

def fetch_data_from_datacite(api_key):
    url = "https://api.datacite.org/dois"

    params = {
        "query":"Alan Turing Institute",
        "page[size]": 25,  # Fetch 25 records per request
    }
    
    all_data = []
    page_number = 1

    # doesn't work:
    #"query": "creators.affiliation.name:'The Alan Turing Institute'",

    while True:
        print(page_number)
        params['page[number]'] = page_number
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = json.loads(response.text)
            all_data.extend(data['data'])  # Assuming the key for the data is 'data'

            # Check if there are more pages
            if data['meta']['totalPages'] > page_number:
                page_number += 1
            else:
                break
        else:
            print(f"Failed to fetch data on page {page_number}: {response.status_code}")
            break

    return all_data

def save_data_to_file(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    api_key = "your_api_key_here"
    all_data = fetch_data_from_datacite(api_key)
    if all_data:
        file_path = os.path.join("..", "data", "datacite_response_data.json")  # Adjust the path as needed
        save_data_to_file(all_data, file_path)
        
