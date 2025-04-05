# базовый URL API
BASE_URL = "https://stellarburgers.nomoreparties.site/api"

# эндпоинты для работы с пользователями
URL_REGISTER = f"{BASE_URL}/auth/register"  # регистрация пользователя
URL_LOGIN = f"{BASE_URL}/auth/login"  # логин пользователя
URL_UPDATE_USER = f"{BASE_URL}/auth/user"  # получение и изменение данных пользователя
URL_DELETE_USER = f"{BASE_URL}/auth/user"  # удаление пользователя

# эндпоинты для работы с заказами
URL_ORDERS = f"{BASE_URL}/orders"  # создание заказа / получение заказов пользователя
