from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import FORGOT_PASSWORD_URL
from locators.locators import ForgotPasswordPageLocators, ResetPasswordPageLocators


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(FORGOT_PASSWORD_URL)
        self.wait.until(EC.visibility_of_element_located(ForgotPasswordPageLocators.RESTORE_BUTTON))
        return self

    def enter_email_and_restore(self, email):
        self.wait.until(EC.visibility_of_element_located(ForgotPasswordPageLocators.EMAIL_INPUT)).send_keys(email)
        button = self.driver.find_element(*ForgotPasswordPageLocators.RESTORE_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', button)
        self.wait.until(EC.url_contains('/reset-password'))

    def is_reset_password_page_opened(self):
        return 'reset-password' in self.driver.current_url


class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_show_password(self):
        icon = self.wait.until(EC.element_to_be_clickable(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON))
        try:
            icon.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', icon)

    def is_password_field_active(self):
        return self.wait.until(
            EC.visibility_of_element_located(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
        ).is_displayed()
