from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import FEED_URL
from locators.locators import FeedPageLocators, MainPageLocators


class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(FEED_URL)
        self.wait.until(EC.visibility_of_element_located(FeedPageLocators.TOTAL_COMPLETED))
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for overlay in overlays:
            if overlay.is_displayed():
                self.wait.until(EC.invisibility_of_element(overlay))
        return self

    def click_order(self):
        link = self.wait.until(EC.element_to_be_clickable(FeedPageLocators.ORDER_LINK))
        try:
            link.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', link)

    def is_modal_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(FeedPageLocators.MODAL)).is_displayed()

    def get_total_completed(self):
        numbers = self.wait.until(EC.presence_of_all_elements_located(FeedPageLocators.TOTAL_COMPLETED))
        return int(numbers[0].text)

    def get_total_completed_today(self):
        numbers = self.wait.until(EC.presence_of_all_elements_located(FeedPageLocators.TOTAL_COMPLETED))
        return int(numbers[1].text)

    def get_in_progress_orders(self):
        self.wait.until(EC.presence_of_element_located(FeedPageLocators.IN_PROGRESS_ORDERS))
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)
        return [element.text.lstrip('0') for element in elements if element.text.strip()]

    def get_order_numbers(self):
        self.wait.until(EC.presence_of_element_located(FeedPageLocators.ORDER_NUMBER_IN_FEED))
        elements = self.driver.find_elements(*FeedPageLocators.ORDER_NUMBER_IN_FEED)
        return [element.text.lstrip('#0') for element in elements if element.text.strip()]
