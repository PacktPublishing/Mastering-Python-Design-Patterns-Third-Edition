import logging
import random
import requests
import tenacity

logging.basicConfig(level=logging.DEBUG)


# The URL of the hypothetical API
API_URL = "http://localhost:5000/api"

@tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_fixed(2))
def fetch_data_from_api():
    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch data from the API: {str(e)}")


if __name__ == "__main__":
    try:
        data = fetch_data_from_api()
        print("Data successfully fetched:", data)
    except RuntimeError as e:
        print(f"Error: {str(e)}")
