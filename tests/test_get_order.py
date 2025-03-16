import requests
import allure
from urls import URL_ORDERS
from data import TextErr


class TestGetOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_with_auth(self, create_user):
        user_data, access_token, _ = create_user
        headers = {"Authorization": access_token}
        response = requests.get(URL_ORDERS, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Получение заказов без авторизации")
    def test_get_orders_without_auth(self):
        response = requests.get(URL_ORDERS)
        assert response.status_code == 401
        assert response.json().get("message") == TextErr.ERROR_AUTH
