import config
from locators import Auth
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    path = config.FORGOT_PASSWORD_PATH

    def submit_email(self, email):
        self.visible(Auth.EMAIL).send_keys(email)
        self.click(Auth.SUBMIT)
