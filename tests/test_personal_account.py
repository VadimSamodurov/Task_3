import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.epic('Stellar Burgers UI')
@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Переход по клику на Личный кабинет')
    def test_go_to_personal_account(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().login(user_data['email'], user_data['password'])

        MainPage(driver).click_personal_account()
        profile_page = ProfilePage(driver).wait_until_opened()

        assert profile_page.is_profile_opened()

    @allure.title('Переход в раздел История заказов')
    def test_go_to_order_history(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().login(user_data['email'], user_data['password'])
        MainPage(driver).click_personal_account()

        profile_page = ProfilePage(driver).wait_until_opened()
        profile_page.click_order_history()

        assert profile_page.is_order_history_opened()

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().login(user_data['email'], user_data['password'])
        MainPage(driver).click_personal_account()

        profile_page = ProfilePage(driver).wait_until_opened()
        profile_page.click_logout()

        assert profile_page.is_login_page_opened()
