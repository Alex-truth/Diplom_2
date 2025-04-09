API-тесты для сервиса Stellar Burgers
Цель проекта:
Проверка стабильности и корректности работы ключевых API-эндпоинтов веб-сервиса Stellar Burgers. Тесты написаны с использованием pytest, requests, allure-pytest.

 Что протестировано
 Пользователь
Успешное создание уникального пользователя

Обработка повторной регистрации

Ошибка при отсутствии обязательных полей

 Авторизация
Логин с корректными данными

Ошибки при неверном логине или пароле

 Изменение данных пользователя
С авторизацией: возможность редактирования любых полей

Без авторизации: проверка недопуска и соответствующей ошибки

Создание заказа
Авторизованный и неавторизованный пользователь

С ингредиентами и без

Ошибка при неверных хэшах ингредиентов

 Получение заказов пользователя
Запрос заказов от авторизованного пользователя

Проверка запрета доступа для неавторизованных
Структура проекта
tests/ — автотесты сгруппированы по эндпоинтам (User, Auth, Orders и др.)

data/ — генерация и хранение тестовых данных

helpers.py/ — генерация необходимых данных через библиотеку random

conftest.py — фикстуры и pre/post-условия

allure-results/ — отчёты 

 



