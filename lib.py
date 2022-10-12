import requests

def get_data(link:str) -> dict:
    return requests.get(link).json()
