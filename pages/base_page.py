from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import MainPageLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.wait_overlays_gone()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', element)

    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def url_contains(self, path):
        return path in self.get_current_url()

    def wait_for_url_contains(self, path):
        self.wait.until(EC.url_contains(path))

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_displayed(self, locator):
        return self.wait_for_visibility(locator).is_displayed()

    def has_visible_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return any(element.is_displayed() for element in elements)

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    def wait_overlays_gone(self):
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for overlay in overlays:
            if overlay.is_displayed():
                self.wait.until(EC.invisibility_of_element(overlay))

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).click_and_hold(source).pause(0.5).move_to_element(target).pause(0.5).release().perform()
        ActionChains(self.driver).drag_and_drop(source, target).perform()
