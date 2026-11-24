from selenium.webdriver.common.by import By

import config


class Header:
    CONSTRUCTOR = (By.CSS_SELECTOR, f'header nav li a[href="{config.CONSTRUCTOR_PATH}"]')
    FEED = (By.CSS_SELECTOR, f'header a[href="{config.FEED_PATH}"]')
    ACCOUNT = (By.CSS_SELECTOR, f'header a[href="{config.ACCOUNT_PATH}"]')


class Auth:
    EMAIL = (By.CSS_SELECTOR, 'form input[name="name"]')
    PASSWORD = (By.CSS_SELECTOR, 'form input[type="password"]')
    SUBMIT = (By.CSS_SELECTOR, 'form button[type="submit"], form button:not([type])')
    FORGOT = (By.LINK_TEXT, "Восстановить пароль")
    RESET_CODE = (By.XPATH, "//label[contains(.,'код из письма') or contains(.,'Код из письма')]/following-sibling::input")
    EYE = (By.CSS_SELECTOR, "form .input__icon-action")
    ACTIVE_PASSWORD = (By.CSS_SELECTOR, "form .input_status_active input[name='Введите новый пароль']")


class Profile:
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    HISTORY = (By.LINK_TEXT, "История заказов")
    LOGOUT = (By.XPATH, "//button[text()='Выход']")


class Constructor:
    TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN = (By.CSS_SELECTOR, f'a[href^="{config.INGREDIENT_PREFIX}"]')
    BUN_NAME = (By.CSS_SELECTOR, f'a[href^="{config.INGREDIENT_PREFIX}"] [class*="ingredient__text"]')
    BUN_COUNT = (By.CSS_SELECTOR, f'a[href^="{config.INGREDIENT_PREFIX}"] [class*="counter_counter__num"]')
    BASKET = (By.CSS_SELECTOR, '[class*="BurgerConstructor_basket__list__"]')
    PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")


class Modal:
    OPEN = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"]')
    DETAILS = (By.XPATH, "//*[contains(@class,'Modal_modal_opened')]//*[text()='Детали ингредиента']")
    CLOSE = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] button[class*="close"]')
    ORDER_NUMBER = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] h2[class*="digits"]')
    DETAIL_NUMBER = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] [class*="Modal_orderBox"] > p:first-child')
    COMPOSITION = (By.XPATH, "//*[contains(@class,'Modal_modal_opened')]//*[text()='Cостав' or text()='Состав']")


class Feed:
    TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    CARD_NUMBER = (By.CSS_SELECTOR, '[class*="OrderHistory_textBox"] p:first-child')
    FIRST_ORDER = (By.CSS_SELECTOR, f'a[href^="{config.FEED_ORDER_PREFIX}"]')
    TOTAL = (By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p")
    TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS = (By.XPATH, "//*[text()='В работе:']/following-sibling::ul[2]")

    @staticmethod
    def order_card(prefix, number):
        return (By.XPATH, f"//a[starts-with(@href,'{prefix}')]//p[text()='#{number:06d}']")
