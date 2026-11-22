import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


@allure.feature("Конструктор и навигация")
class TestConstructor:
    @allure.title("Переход из ленты в конструктор")
    def test_open_constructor(self, driver):
        feed = FeedPage(driver)
        feed.open()
        feed.go_to_constructor()

        assert ConstructorPage(driver).title() == "Соберите бургер"

    @allure.title("Переход из конструктора в ленту заказов")
    def test_open_feed(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.go_to_feed()

        assert FeedPage(driver).title() == "Лента заказов"

    @allure.title("Детали содержат название выбранного ингредиента")
    def test_ingredient_details(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open()
        name = constructor.bun_name()
        constructor.open_bun_details()

        assert name in constructor.ingredient_details()

    @allure.title("Крестик закрывает детали ингредиента")
    def test_close_ingredient_details(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.open_bun_details()
        constructor.ingredient_details()
        constructor.close_modal()

        assert constructor.modal_closed()

    @allure.title("Добавление булки увеличивает её счётчик на две половины")
    def test_ingredient_counter(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open()
        before = constructor.bun_count()
        constructor.add_bun()

        assert constructor.bun_count() == before + 2

    @allure.title("Пользователь получает номер оформленного в конструкторе заказа")
    def test_place_order(self, signed_in):
        signed_in.add_bun()
        signed_in.place_order()

        assert signed_in.confirmed_order_number() > 0
