from locators import Feed
from pages.base_page import BasePage


class HistoryPage(BasePage):
    path = "/account/order-history"

    def order_number(self, number):
        return self.visible(Feed.order_card("/account/order-history/", number)).text
