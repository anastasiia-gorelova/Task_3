from locators import Constructor, Modal
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def title(self):
        return self.visible(Constructor.TITLE).text

    def bun_name(self):
        return self.visible(Constructor.BUN_NAME).text

    def open_bun_details(self):
        self.click(Constructor.BUN)

    def ingredient_details(self):
        self.visible(Modal.DETAILS)
        return self.visible(Modal.OPEN).text.splitlines()

    def add_bun(self):
        bun = self.visible(Constructor.BUN)
        basket = self.visible(Constructor.BASKET)
        self.execute_script("""
            const [source, target] = arguments;
            const dataTransfer = new DataTransfer();
            for (const [element, type] of [[source, 'dragstart'], [target, 'dragenter'],
                    [target, 'dragover'], [target, 'drop'], [source, 'dragend']]) {
                element.dispatchEvent(new DragEvent(type, {
                    bubbles: true, cancelable: true, dataTransfer
                }));
            }
        """, bun, basket)

    def bun_count(self):
        return int(self.visible(Constructor.BUN_COUNT).text)

    def place_order(self):
        self.click(Constructor.PLACE_ORDER)

    def confirmed_order_number(self):
        def number_ready(driver):
            text = self.visible(Modal.ORDER_NUMBER).text.strip()
            return text.isdigit() and int(text)
        return self.wait.until(number_ready)
