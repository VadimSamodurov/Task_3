import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.epic('Stellar Burgers UI')
@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Переход по клику на Конструктор')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_order_feed()
        main_page.click_constructor()

        assert main_page.is_constructor_opened()

    @allure.title('Переход по клику на Лента заказов')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_order_feed()

        assert main_page.is_order_feed_opened()

    @allure.title('Клик на ингредиент открывает всплывающее окно')
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_ingredient()

        assert main_page.is_modal_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_ingredient()
        assert main_page.is_modal_displayed()
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title('При добавлении ингредиента увеличивается каунтер')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver).open()
        ingredient = main_page.add_ingredient_to_order()

        assert main_page.get_ingredient_counter(ingredient) > 0

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().login(user_data['email'], user_data['password'])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.click_place_order()
        order_number = main_page.get_order_number()

        assert order_number.isdigit()
        assert int(order_number) > 0
