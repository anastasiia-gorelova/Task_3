from locators import Feed, Modal
from pages.base_page import BasePage


class FeedPage(BasePage):
    path = "/feed"

    def title(self):
        return self.visible(Feed.TITLE).text

    def open_first_order(self):
        card = self.visible(Feed.FIRST_ORDER)
        number = int(card.find_element(*Feed.CARD_NUMBER).text.lstrip("#"))
        self.click(Feed.order_card("/feed/", number))
        return f"#{number:06d}"

    def detail_number(self):
        self.visible(Modal.COMPOSITION)
        return self.visible(Modal.DETAIL_NUMBER).text

    def order_number(self, number):
        return self.visible(Feed.order_card("/feed/", number)).text

    def total(self):
        return int(self.visible(Feed.TOTAL).text)

    def today(self):
        return int(self.visible(Feed.TODAY).text)

    def wait_for_total_above(self, previous):
        return self.wait.until(lambda _: self.total() > previous)

    def wait_for_today_above(self, previous):
        return self.wait.until(lambda _: self.today() > previous)

    def watch_in_progress(self):
        # Заказ может сменить статус до ответа POST. Сохраняем номера,
        # показанные в этом списке с момента начала наблюдения.
        self.driver.execute_script("""
            const list = arguments[0];
            window.observedOrders = new Set();
            const read = () => {
                for (const item of list.querySelectorAll('li')) {
                    window.observedOrders.add(Number(item.textContent.trim()));
                }
            };
            new MutationObserver(read).observe(list, {
                childList: true, characterData: true, subtree: true
            });
            read();
        """, self.visible(Feed.IN_PROGRESS))

    def saw_in_progress(self, number):
        return self.wait.until(lambda d: d.execute_script(
            "return window.observedOrders.has(arguments[0])", number))
