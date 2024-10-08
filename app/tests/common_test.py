import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a remote WebDriver instance
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        options=chrome_options
    )

    yield driver  # Provide the fixture value to the test

    driver.quit()  # Cleanup after tests