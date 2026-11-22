import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestRecovery:
    @allure.title("Ссылка на форме входа открывает восстановление пароля")
    def test_open_recovery(self, driver):
        login = LoginPage(driver)
        login.open()
        login.recover_password()

        assert ForgotPasswordPage(driver).at_page()

    @allure.title("Отправка почты открывает форму с кодом из письма")
    def test_submit_email(self, driver, user):
        recovery = ForgotPasswordPage(driver)
        recovery.open()
        recovery.submit_email(user[0]["email"])

        assert ResetPasswordPage(driver).code_field_visible()

    @allure.title("Кнопка видимости показывает пароль и подсвечивает поле")
    def test_password_field_highlight(self, driver, user):
        recovery = ForgotPasswordPage(driver)
        recovery.open()
        recovery.submit_email(user[0]["email"])
        reset = ResetPasswordPage(driver)
        reset.toggle_password_visibility()

        assert reset.active_password_type() == "text"
