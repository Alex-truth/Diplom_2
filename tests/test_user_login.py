import pytest
import allure
import requests

from data import TextErr
from urls import URL_LOGIN
from helpers import random_password, random_email


class TestUserLogin:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):
        user_data, _, response = create_user
        response = requests.post(URL_LOGIN, json={
            "email": user_data["email"],
            "password": user_data["password"]
        })
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Логин с неверным паролем")
    def test_login_invalid_password(self, create_user):
        user_data, _, response = create_user
        password = random_password()

        response = requests.post(URL_LOGIN, json={
            "email": user_data["email"],
            "password": password
        })
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_INCORRECT_MAIL_OR_PASS

    @allure.title("Логин с неверным email")
    def test_login_invalid_email(self, create_user):
        user_data, _, response = create_user
        email = random_email()

        response = requests.post(URL_LOGIN, json={
            "email": email,
            "password": user_data["password"]
        })
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_INCORRECT_MAIL_OR_PASS
