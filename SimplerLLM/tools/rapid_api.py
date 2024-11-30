# SimplerLLM/tools/rapid_api.py

import requests
import load_dotenv


class RapidAPIClient:
    def __init__(self):
        # Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
        self.api_key = "cd81f965a0msh1be871598b544e8p1d5b11jsnfd46eecca3dc"
        self.base_headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "website-seo-analyzer.p.rapidapi.com"  # Adjust as needed for the specific API
        }

    def call_api(self, api_url, method='GET', params=None):
        response = requests.request(method, api_url, headers=self.base_headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
