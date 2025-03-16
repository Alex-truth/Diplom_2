import random
import string
import allure


@allure.title("Генерирует случайную строку из букв и цифр")
def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

@allure.title("Генерирует случайный email")
def random_email():
    return f"{generate_random_string(10)}@gmail.com"


@allure.title("Генерирует случайный пароль")
def random_password():
    return generate_random_string(10)


@allure.title("Генерирует случайное имя")
def random_name():
    return generate_random_string(8)

