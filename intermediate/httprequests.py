import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_url = os.getenv("API_URL")

jsonResponse = requests.get(api_url).json()

print(jsonResponse)