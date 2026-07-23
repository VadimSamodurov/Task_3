## Задание 3: UI-тесты Stellar Burgers

### Реализованные сценарии

- Восстановление пароля
- Личный кабинет
- Основной функционал конструктора
- Лента заказов

Автотесты запускаются в Google Chrome и Mozilla Firefox.

### Структура проекта

- `pages` — Page Object для страниц приложения
- `locators` — локаторы элементов
- `helpers` — создание/удаление пользователя через API
- `tests` — UI-тесты, разделённые по функциональности
- `data` — URL страниц

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск тестов**

> `$ pytest`

**Запуск с Allure**

> `$ pytest --alluredir=allure-results`
>
> `$ allure serve allure-results`
