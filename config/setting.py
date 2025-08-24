from config.base_requests import post_request
from config.endpoints import AUTH_URL


def get_token(user,password):
    body = {
        "username": user,
        "password": password
    }
    response = post_request(url=AUTH_URL,json=body)
    data = response.json()
    return data['token']