from locators import Auth
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    path = "/reset-password"

    def code_field_visible(self):
        return self.at_page() and self.visible(Auth.RESET_CODE).is_displayed()

    def toggle_password_visibility(self):
        self.click(Auth.EYE)

    def active_password_type(self):
        return self.visible(Auth.ACTIVE_PASSWORD).get_attribute("type")
