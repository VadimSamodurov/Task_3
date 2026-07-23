from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import OrderHistoryPageLocators, ProfilePageLocators


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_opened(self):
        self.wait.until(EC.url_contains('/account'))
        return self

    def click_order_history(self):
        link = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY_LINK))
        try:
            link.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', link)
        self.wait.until(EC.url_contains('/order-history'))

    def click_logout(self):
        button = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
        try:
            button.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', button)
        self.wait.until(EC.url_contains('/login'))

    def is_profile_opened(self):
        return '/account/profile' in self.driver.current_url or '/account' in self.driver.current_url

    def is_order_history_opened(self):
        return '/account/order-history' in self.driver.current_url


class OrderHistoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_order_numbers(self):
        self.wait.until(EC.visibility_of_element_located(OrderHistoryPageLocators.ORDER_NUMBER))
        elements = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_NUMBER)
        return [element.text.lstrip('#0') for element in elements if element.text.strip()]
