from data.urls import LOGIN_PAGE_URL, MAIN_PAGE_URL
from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.open_url(LOGIN_PAGE_URL)
        self.wait_for_visibility(LoginPageLocators.LOGIN_BUTTON)
        self.wait_overlays_gone()
        return self

    def click_restore_password(self):
        self.click_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    def login(self, email, password):
        self.fill_field(LoginPageLocators.EMAIL_INPUT, email)
        self.fill_field(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url(MAIN_PAGE_URL)

    def is_forgot_password_page_opened(self):
        return self.url_contains('forgot-password')

    def is_login_page_opened(self):
        return self.url_contains('login')
