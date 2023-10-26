import os
import requests
import pandas as pd


def fetch_data_and_filter(file_path, api_key, query, filter):
    url = "https://api.core.ac.uk/v3/search/works/"

    params = {"api_key": api_key, "q": query, "scroll": True, "limit": 1000}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return response.status_code

    df = pd.DataFrame(response.json()["results"])

    df_filtered = df[df["fullText"].str.lower().str.contains(filter)]

    df_filtered = df_filtered.drop(columns=["fullText"])

    df_filtered.to_csv(file_path, index=False)

    print(f"Total results: {len(df)}")
    print(f"Filtered results: {len(df_filtered)}")


if __name__ == "__main__":
    api_key = "your_api_key"
    query = "The Alan Turing Institute"
    filter = "alan turing institute"
    file_path = os.path.join("..", "data", "core_filtered_response_data.csv")

    fetch_data_and_filter(file_path, api_key, query, filter)
