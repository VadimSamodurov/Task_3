import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import OrderHistoryPage, ProfilePage
from helpers.api_helper import create_order


@allure.epic('Stellar Burgers UI')
@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Клик на заказ открывает всплывающее окно')
    def test_order_modal_opens(self, driver):
        feed_page = FeedPage(driver).open()
        feed_page.click_order()

        assert feed_page.is_modal_displayed()

    @allure.title('Заказы пользователя из Истории заказов отображаются в Ленте заказов')
    def test_user_orders_displayed_in_feed(self, driver, user):
        user_data, access_token = user
        order = create_order(access_token)
        order_number = str(order['order']['number']).lstrip('0')

        LoginPage(driver).open().login(user_data['email'], user_data['password'])
        MainPage(driver).click_personal_account()
        ProfilePage(driver).wait_until_opened().click_order_history()
        history_numbers = [n.lstrip('0') for n in OrderHistoryPage(driver).get_order_numbers()]

        MainPage(driver).click_order_feed()
        feed_numbers = [n.lstrip('0') for n in FeedPage(driver).get_order_numbers()]

        assert order_number in history_numbers
        assert order_number in feed_numbers

    @allure.title('После создания заказа счётчик Выполнено за всё время увеличивается')
    def test_total_completed_increases(self, driver, user):
        user_data, _ = user
        feed_page = FeedPage(driver).open()
        total_before = feed_page.get_total_completed()

        LoginPage(driver).open().login(user_data['email'], user_data['password'])
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.click_place_order()
        main_page.get_order_number()
        main_page.close_modal()

        MainPage(driver).click_order_feed()
        total_after = FeedPage(driver).get_total_completed()

        assert total_after > total_before

    @allure.title('После создания заказа счётчик Выполнено за сегодня увеличивается')
    def test_total_completed_today_increases(self, driver, user):
        user_data, _ = user
        feed_page = FeedPage(driver).open()
        total_before = feed_page.get_total_completed_today()

        LoginPage(driver).open().login(user_data['email'], user_data['password'])
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.click_place_order()
        main_page.get_order_number()
        main_page.close_modal()

        MainPage(driver).click_order_feed()
        total_after = FeedPage(driver).get_total_completed_today()

        assert total_after >= total_before

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_appears_in_progress(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().login(user_data['email'], user_data['password'])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.click_place_order()
        order_number = main_page.get_order_number().lstrip('0')
        main_page.close_modal()

        MainPage(driver).click_order_feed()
        in_progress = [number.lstrip('0') for number in FeedPage(driver).get_in_progress_orders()]

        assert order_number in in_progress
