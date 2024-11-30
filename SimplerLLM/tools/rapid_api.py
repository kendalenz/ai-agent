import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class RapidAPIClient:
    def __init__(self):
        # Use the API key from the .env file
        self.api_key = os.getenv("RAPIDAPI_KEY")
        if not self.api_key:
            raise Exception("RAPIDAPI_KEY not found in .env file")
        self.base_headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "website-seo-analyzer.p.rapidapi.com"  # Adjust as needed for the specific API
        }

    def call_api(self, api_url, method='GET', params=None):
        try:
            response = requests.request(method, api_url, headers=self.base_headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error calling API: {e}")
