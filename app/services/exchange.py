import requests

def get_usd_to_gtq_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    return data["rates"]["GTQ"]