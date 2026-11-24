import config
from locators import Auth
from pages.base_page import BasePage


class LoginPage(BasePage):
    path = config.LOGIN_PATH

    def sign_in(self, user):
        self.visible(Auth.EMAIL).send_keys(user["email"])
        self.visible(Auth.PASSWORD).send_keys(user["password"])
        self.click(Auth.SUBMIT)

    def recover_password(self):
        self.click(Auth.FORGOT)

    def login_form_visible(self):
        return self.at_page() and self.visible(Auth.PASSWORD).is_displayed()
