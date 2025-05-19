import os
import requests
from dotenv import load_dotenv
import time
import hashlib

load_dotenv()

BUNNY_STORAGE_NAME = os.getenv('BUNNY_STORAGE_NAME')
BUNNY_STORAGE_PASSWORD = os.getenv('BUNNY_STORAGE_PASSWORD')
CDN_URL = os.getenv('BUNNY_CDN_URL')

def upload_to_bunny_storage(file):
    file_name = file.name
    url = f"https://storage.bunnycdn.com/{BUNNY_STORAGE_NAME}/{file_name}"
    headers = {
        "AccessKey": BUNNY_STORAGE_PASSWORD,
        "Content-Type": "application/octet-stream",
    }
    file_content = file.read()
    response = requests.put(url, headers=headers, data=file_content)
   
    if response.status_code == 201:
        return f"{CDN_URL}/{file_name}", file_name
    else:
        return None, None



BUNNY_CDN_URL = os.getenv('BUNNY_CDN_URL')
BUNNY_API_KEY = os.getenv('BUNNY_API_KEY')  

def generate_bunny_token(file_path, expiration=3600):
    expiration_time = int(time.time()) + expiration
    path = '/' + file_path.lstrip('/')
    hash_string = hashlib.sha256((BUNNY_API_KEY + path + str(expiration_time)).encode()).hexdigest()
    token = f"?token={hash_string}&expires={expiration_time}"
    return f"{BUNNY_CDN_URL}/{file_path}{token}"
