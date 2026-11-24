import config
from locators import Feed
from pages.base_page import BasePage


class HistoryPage(BasePage):
    path = config.HISTORY_PATH

    def order_number(self, number):
        return self.visible(Feed.order_card(config.HISTORY_ORDER_PREFIX, number)).text
