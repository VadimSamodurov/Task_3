from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import LOGIN_PAGE_URL, MAIN_PAGE_URL
from locators.locators import LoginPageLocators, MainPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for overlay in overlays:
            if overlay.is_displayed():
                self.wait.until(EC.invisibility_of_element(overlay))
        return self

    def click_restore_password(self):
        link = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.RESTORE_PASSWORD_LINK))
        try:
            link.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', link)

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', button)
        self.wait.until(EC.url_to_be(MAIN_PAGE_URL))
