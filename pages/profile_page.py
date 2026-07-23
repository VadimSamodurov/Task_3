from locators.locators import OrderHistoryPageLocators, ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def wait_until_opened(self):
        self.wait_for_url_contains('/account')
        return self

    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_for_url_contains('/order-history')

    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_url_contains('/login')

    def is_profile_opened(self):
        return self.url_contains('/account')

    def is_order_history_opened(self):
        return self.url_contains('/account/order-history')

    def is_login_page_opened(self):
        return self.url_contains('login')


class OrderHistoryPage(BasePage):
    def get_order_numbers(self):
        elements = self.find_elements(OrderHistoryPageLocators.ORDER_NUMBER)
        return [element.text.lstrip('#0') for element in elements if element.text.strip()]
