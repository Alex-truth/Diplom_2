import requests
import allure
import pytest
from data import TextErr
from urls import URL_REGISTER
from helpers import random_email, random_password, random_name


class TestUserCreation:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_user):
        user_data, _, response = create_user
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_user_already_exists(self, create_user):
        user_data, _, response = create_user
        response = requests.post(URL_REGISTER, json=user_data)
        assert response.status_code == 403
        assert response.json().get("message") == TextErr.ERROR_USER_EXISTS

    @allure.title("Создание пользователя без email")
    def test_create_user_missing_email(self):
        user_data = {
            "password": random_password(),
            "name": random_name()
        }
        response = requests.post(URL_REGISTER, json=user_data)
        assert response.status_code == 403
        assert response.json().get("message") == TextErr.ERROR_REQUIRED_FIELDS

    @allure.title("Создание пользователя без пароля")
    def test_create_user_missing_password(self):
        user_data = {
            "email": random_email(),
            "name": random_name()
        }
        response = requests.post(URL_REGISTER, json=user_data)
        assert response.status_code == 403
        assert response.json().get("message") == TextErr.ERROR_REQUIRED_FIELDS