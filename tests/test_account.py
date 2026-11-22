import allure

from pages.history_page import HistoryPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestAccount:
    @allure.title("Личный кабинет открывает профиль текущего пользователя")
    def test_open_profile(self, driver, signed_in, user):
        signed_in.go_to_account()

        assert ProfilePage(driver).name() == user[0]["name"]

    @allure.title("Из профиля открывается история заказов")
    def test_open_history(self, driver, signed_in):
        signed_in.go_to_account()
        ProfilePage(driver).go_to_history()

        assert HistoryPage(driver).at_page()

    @allure.title("Выход из профиля возвращает пользователя на страницу входа")
    def test_logout(self, driver, signed_in):
        signed_in.go_to_account()
        ProfilePage(driver).logout()

        assert LoginPage(driver).login_form_visible()
