from data.urls import FEED_URL
from locators.locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open(self):
        self.open_url(FEED_URL)
        self.wait_for_visibility(FeedPageLocators.TOTAL_COMPLETED)
        self.wait_overlays_gone()
        return self

    def click_order(self):
        self.click_element(FeedPageLocators.ORDER_LINK)

    def is_modal_displayed(self):
        return self.is_element_displayed(FeedPageLocators.MODAL)

    def get_total_completed(self):
        numbers = self.find_elements(FeedPageLocators.TOTAL_COMPLETED)
        return int(numbers[0].text)

    def get_total_completed_today(self):
        numbers = self.find_elements(FeedPageLocators.TOTAL_COMPLETED)
        return int(numbers[1].text)

    def get_in_progress_orders(self):
        elements = self.find_elements(FeedPageLocators.IN_PROGRESS_ORDERS)
        return [element.text.lstrip('0') for element in elements if element.text.strip()]

    def get_order_numbers(self):
        elements = self.find_elements(FeedPageLocators.ORDER_NUMBER_IN_FEED)
        return [element.text.lstrip('#0') for element in elements if element.text.strip()]
