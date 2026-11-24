import config
from locators import Profile
from pages.base_page import BasePage


class ProfilePage(BasePage):
    path = config.PROFILE_PATH

    def name(self):
        return self.visible(Profile.NAME).get_property("value")

    def go_to_history(self):
        self.click(Profile.HISTORY)

    def logout(self):
        self.click(Profile.LOGOUT)
