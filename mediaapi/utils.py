import os
import requests
from dotenv import load_dotenv

load_dotenv()

BUNNY_STORAGE_NAME = os.getenv('BUNNY_STORAGE_NAME')
STORAGE_PASSWORD = os.getenv('BUNNY_STORAGE_PASSWORD')
CDN_URL = os.getenv('BUNNY_CDN_URL')

def upload_to_bunny_storage(file):
    file_name = file.name
    url = f"https://storage.bunnycdn.com/{BUNNY_STORAGE_NAME}/{file_name}"

    headers = {
        "AccessKey": STORAGE_PASSWORD,
        "Content-Type": "application/octet-stream",
    }

    response = requests.put(url, headers=headers, data=file.read())

    if response.status_code == 201:
        return f"{CDN_URL}/{file_name}", file_name
    else:
        return None, None

