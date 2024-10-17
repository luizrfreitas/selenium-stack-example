import os
import unittest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

load_dotenv()


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        browser = os.getenv('BROWSER', 'chrome')

        grid_url = os.getenv('GRID_URL', 'http://selenium-hub:4444/wd/hub')

        if browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            self.driver: WebDriver = webdriver.Remote(
                command_executor=grid_url,
                options=chrome_options
            )
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            self.driver: WebDriver = webdriver.Remote(
                command_executor=grid_url,
                options=firefox_options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
