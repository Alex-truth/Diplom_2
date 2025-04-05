import pytest
import requests
from urls import URL_REGISTER, URL_DELETE_USER, URL_LOGIN
from helpers import random_email, random_password, random_name


@pytest.fixture
def create_user():
    user_data = {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }
    response = requests.post(URL_REGISTER, json=user_data)
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(URL_LOGIN, json=login_data)
    access_token = login_response.json().get("accessToken")
    yield user_data, access_token, response

    headers = {"Authorization": f"Bearer {access_token}"}
    requests.delete(URL_DELETE_USER, headers=headers)