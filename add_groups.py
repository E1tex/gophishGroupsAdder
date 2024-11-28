import csv
import requests
import argparse
from urllib.parse import urlparse

API_KEY = 'HARDCODE_YOUR_API_KEY_HERE'
HEADERS = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json'
}

def validate_and_format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        raise ValueError("URL должен содержать схему (http или https).")
    if not parsed_url.netloc:
        raise ValueError("URL должен содержать домен или IP-адрес.")
    if not url.endswith('/api'):
        url = url.rstrip('/') + '/api'
    
    return url

def create_user_group(first_name, surname, last_name, email, gophish_url):
    group_name = f"{last_name} {first_name} {surname}"
    group_data = {
        "name": group_name,
        "targets": [
            {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "position": ""
            }
        ]
    }
    response = requests.post(f'{gophish_url}/groups/', headers=HEADERS, json=group_data)
    if response.status_code == 201:
        print(f"Group '{group_name}' created successfully.")
        return response.json()['id']
    else:
        print(f"Failed to create group '{group_name}': {response.text}")
        return None

def get_user_groups(gophish_url):
    response = requests.get(f'{gophish_url}/groups', headers=HEADERS)
    if response.status_code == 200:
        return {group['name']: group['id'] for group in response.json()}
    else:
        print(f"Failed to retrieve user groups: {response.text}")
        return {}

def process_csv(file_path, gophish_url):
    user_groups = get_user_groups(gophish_url)
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            group_name = f"{row['last_name']} {row['name']} {row['surname']}"
            if group_name not in user_groups:
                group_id = create_user_group(row['name'], row['surname'], row['last_name'], row['email'], gophish_url)
                if group_id is not None:
                    user_groups[group_name] = group_id
            else:
                print(f'Group "{group_name}" exists')

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file to create user groups in Gophish. Example: python add_groups.py users.csv "https://example.com:3333/api"')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing user data.')
    parser.add_argument('gophish_url', type=str, help='URL of the Gophish API (e.g., https://example.com:3333/api).')
    
    args = parser.parse_args()
    
    try:
        gophish_url = validate_and_format_url(args.gophish_url)
    except ValueError as e:
        print(f"Invalid Gophish URL: {e}")
        return

    process_csv(args.csv_file, gophish_url)

if __name__ == "__main__":
    main()
