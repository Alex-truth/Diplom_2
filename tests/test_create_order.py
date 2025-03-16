import requests
import allure
from data import INGREDIENTS
from urls import URL_ORDERS
from data import TextErr


class TestOrderCreation:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, create_user):
        user_data, access_token, _ = create_user
        order_data = {"ingredients": INGREDIENTS}
        headers = {"Authorization": access_token}
        response = requests.post(URL_ORDERS, json=order_data, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        order_data = {"ingredients": INGREDIENTS}
        response = requests.post(URL_ORDERS, json=order_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, create_user):
        user_data, access_token, _ = create_user
        order_data = {"ingredients": INGREDIENTS}
        headers = {"Authorization": access_token}
        response = requests.post(URL_ORDERS, json=order_data, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_user):
        user_data, access_token, _ = create_user
        order_data = {"ingredients": []}
        headers = {"Authorization": access_token}
        response = requests.post(URL_ORDERS, json=order_data, headers=headers)
        assert response.status_code == 400
        assert response.json().get("message") == TextErr.ERROR_INGREDIENT

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_user):
        user_data, access_token, _ = create_user
        order_data = {"ingredients": ["no_ingr_value"]}
        headers = {"Authorization": access_token}
        response = requests.post(URL_ORDERS, json=order_data, headers=headers)
        assert response.status_code == 500