from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL
from locators import Header, Modal


class BasePage:
    path = "/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(BASE_URL + self.path)

    def visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def click(self, locator):
        def click_when_ready(driver):
            element = ec.element_to_be_clickable(locator)(driver)
            if not element:
                return False
            try:
                element.click()
                return True
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False

        self.wait.until(click_when_ready)

    def at_page(self):
        return self.wait.until(ec.url_to_be(BASE_URL + self.path))

    def go_to_constructor(self):
        self.click(Header.CONSTRUCTOR)

    def go_to_feed(self):
        self.click(Header.FEED)

    def go_to_account(self):
        self.click(Header.ACCOUNT)

    def close_modal(self):
        self.click(Modal.CLOSE)

    def modal_closed(self):
        return self.wait.until(ec.invisibility_of_element_located(Modal.OPEN))
