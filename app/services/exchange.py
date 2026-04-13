import requests

def get_usd_to_gtq_rate():
    return 7.8
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error obteniendo tipo de cambio")

    data = response.json()
    
    return data["rates"]["GTQ"]