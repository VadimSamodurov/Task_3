from data.urls import FORGOT_PASSWORD_URL
from locators.locators import ForgotPasswordPageLocators, ResetPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def open(self):
        self.open_url(FORGOT_PASSWORD_URL)
        self.wait_for_visibility(ForgotPasswordPageLocators.RESTORE_BUTTON)
        return self

    def enter_email_and_restore(self, email):
        self.fill_field(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.wait_for_url_contains('/reset-password')

    def is_reset_password_page_opened(self):
        return self.url_contains('reset-password')


class ResetPasswordPage(BasePage):
    def click_show_password(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        return self.is_element_displayed(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
