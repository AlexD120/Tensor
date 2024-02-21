import os
from dotenv import load_dotenv
from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tensor.utils import allure_attach
from tensor.helpers import dates


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="100.0")


@pytest.fixture(scope='function')
def browser_config(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    browser.config.base_url = dates.BASE_URL
    browser.config.window_width = 1440
    browser.config.window_height = 900
    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications-prompt")

    yield browser

    allure_attach.add_html(browser)
    allure_attach.add_screenshot(browser)
    allure_attach.add_logs(browser)
    allure_attach.add_video(browser)

    browser.quit()
