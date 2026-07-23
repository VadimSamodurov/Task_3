import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_pages import ForgotPasswordPage, ResetPasswordPage


@allure.epic('Stellar Burgers UI')
@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver).open()
        login_page.click_restore_password()

        assert 'forgot-password' in driver.current_url

    @allure.title('Ввод почты и клик по кнопке Восстановить')
    def test_enter_email_and_click_restore(self, driver, user):
        user_data, _ = user
        login_page = LoginPage(driver).open()
        login_page.click_restore_password()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email_and_restore(user_data['email'])

        assert forgot_page.is_reset_password_page_opened()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_show_password_makes_field_active(self, driver, user):
        user_data, _ = user
        LoginPage(driver).open().click_restore_password()
        ForgotPasswordPage(driver).enter_email_and_restore(user_data['email'])

        reset_page = ResetPasswordPage(driver)
        reset_page.click_show_password()

        assert reset_page.is_password_field_active()
