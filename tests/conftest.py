from uuid import uuid4

import allure
import pytest
import requests
from selenium import webdriver

from config import BASE_URL
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    allure.dynamic.label("browser", browser)
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        instance = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        instance = webdriver.Firefox(options=options)
    try:
        instance.set_window_size(1440, 1000)
        yield instance
    finally:
        instance.quit()


@pytest.fixture
def user():
    data = {"email": f"ui-{uuid4().hex}@example.com", "password": uuid4().hex, "name": "Stellar Tester"}
    response = requests.post(f"{BASE_URL}/api/auth/register", json=data, timeout=30)
    response.raise_for_status()
    token = response.json()["accessToken"]
    try:
        yield data, token
    finally:
        requests.delete(f"{BASE_URL}/api/auth/user", headers={"Authorization": token},
                        timeout=30).raise_for_status()


@pytest.fixture
def signed_in(driver, user):
    login = LoginPage(driver)
    login.open()
    login.sign_in(user[0])
    constructor = ConstructorPage(driver)
    constructor.at_page()
    return constructor


@pytest.fixture
def create_order(user):
    catalog = requests.get(f"{BASE_URL}/api/ingredients", timeout=20)
    catalog.raise_for_status()
    items = catalog.json()["data"]
    ingredients = [next(item["_id"] for item in items if item["type"] == kind)
                   for kind in ("bun", "main")]

    def create():
        response = requests.post(
            f"{BASE_URL}/api/orders", json={"ingredients": ingredients},
            headers={"Authorization": user[1]}, timeout=45,
        )
        response.raise_for_status()
        return response.json()["order"]["number"]

    return create
