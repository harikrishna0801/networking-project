import requests

from config import SERVER_URL


def send(data):
    try:
        response = requests.post(SERVER_URL, json=data, timeout=10)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to reach server:", e)
