import pytest
import allure
import requests
from urls import URL_UPDATE_USER
from helpers import random_email, random_name
from data import TextErr


class TestUserUpdate:
    allure.title('Изменение email после авторизации')
    def test_update_email_with_auth(self, create_user):
        user_data, access_token, _ = create_user
        updated_data = {"email": random_email()}
        headers = {"Authorization": access_token}
        response = requests.patch(URL_UPDATE_USER, json=updated_data, headers=headers)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Изменение пароля после авторизации")
    def test_update_password_with_auth(self, create_user):
        user_data, access_token, _ = create_user
        updated_data = {"password": random_email()}
        headers = {"Authorization": access_token}
        response = requests.patch(URL_UPDATE_USER, json=updated_data, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Изменение имени после авторизации")
    def test_update_name_with_auth(self, create_user):
        user_data, access_token, _ = create_user
        updated_data = {"name": random_name()}
        headers = {"Authorization": access_token}
        response = requests.patch(URL_UPDATE_USER, json=updated_data, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Изменение email без авторизации")
    def test_update_email_without_auth(self, create_user):
        user_data, _, _ = create_user
        updated_data = {"email": random_email()}
        response = requests.patch(URL_UPDATE_USER, json=updated_data)
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_AUTH

    @allure.title("Изменение пароля без авторизации")
    def test_update_password_without_auth(self, create_user):
        user_data, _, _ = create_user
        updated_data = {"password": random_email()}
        response = requests.patch(URL_UPDATE_USER, json=updated_data)
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_AUTH

    @allure.title("Изменение имени без авторизации")
    def test_update_name_without_auth(self, create_user):
        user_data, _, _ = create_user
        updated_data = {"name": random_name()}
        response = requests.patch(URL_UPDATE_USER, json=updated_data)
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_AUTH

    @allure.title("Изменение почтового адреса на существующий email")
    def test_update_email_to_existing_email(self, create_user):
        user_data, access_token, _ = create_user
        existing_email = "existing@example.com"
        updated_data = {"email": existing_email}
        headers = {"Authorization": access_token}
        response = requests.patch(URL_UPDATE_USER, json=updated_data, headers=headers)
        assert response.status_code == 403
        assert response.json().get("message") == TextErr.ERROR_EXISTS_EMAIL
