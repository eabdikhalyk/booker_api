import pytest
import os
from dotenv import load_dotenv
from config.setting import get_token


@pytest.fixture(scope="session")
def client_headers():
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    token = get_token(user,password)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Cookie": f"token={token}",
        'Authorization': f'Basic {token}'
    }
    return headers
