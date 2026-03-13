import requests
import random

API_URL = "https://api.electricitymap.org/v3/carbon-intensity/latest?zone=IN"

def get_carbon_intensity(api_key):

    headers = {
        "auth-token": api_key
    }

    try:
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()

            carbon = data.get("carbonIntensity")

            if carbon:
                return carbon

        # If API fails → simulate carbon value
        print("Using sandbox simulated carbon data")

        return random.randint(200, 800)

    except Exception as e:
        print("API failed → using simulated carbon value")

        return random.randint(200, 800)