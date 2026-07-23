import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers.api_helper import create_user, delete_user

CHROMEDRIVER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'drivers',
    'chromedriver'
)


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver_instance = webdriver.Chrome(
            service=ChromeService(executable_path=CHROMEDRIVER_PATH),
            options=options
        )
    else:
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver_instance = webdriver.Firefox(options=options)

    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def user():
    user_data, access_token = create_user()
    yield user_data, access_token
    delete_user(access_token)
