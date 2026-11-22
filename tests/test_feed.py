import allure

from pages.feed_page import FeedPage
from pages.history_page import HistoryPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
class TestFeed:
    @allure.title("Детали заказа показывают номер выбранной карточки")
    def test_order_details(self, driver):
        feed = FeedPage(driver)
        feed.open()
        number = feed.open_first_order()

        assert feed.detail_number() == number

    @allure.title("Заказ из личной истории виден в общей ленте")
    def test_history_order_in_feed(self, driver, signed_in, create_order):
        number = create_order()
        signed_in.go_to_account()
        ProfilePage(driver).go_to_history()
        history = HistoryPage(driver)
        expected = history.order_number(number)
        history.go_to_feed()

        assert FeedPage(driver).order_number(number) == expected

    @allure.title("Заказ увеличивает число выполненных за всё время")
    def test_total_counter(self, driver, create_order):
        feed = FeedPage(driver)
        feed.open()
        before = feed.total()
        number = create_order()
        feed.order_number(number)

        assert feed.wait_for_total_above(before)

    @allure.title("Заказ увеличивает число выполненных за сегодня")
    def test_today_counter(self, driver, create_order):
        feed = FeedPage(driver)
        feed.open()
        before = feed.today()
        number = create_order()
        feed.order_number(number)

        assert feed.wait_for_today_above(before)

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_order_in_progress(self, driver, create_order):
        feed = FeedPage(driver)
        feed.open()
        feed.watch_in_progress()
        number = create_order()

        assert feed.saw_in_progress(number)
