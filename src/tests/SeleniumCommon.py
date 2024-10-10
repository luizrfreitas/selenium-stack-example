from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumCommon:

    driver = None

    def __init__(self):
        self.set_driver()

    @classmethod
    def set_driver(cls):
        if cls.driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            cls.driver = webdriver.Remote(
                command_executor='http://selenium-hub:4444/wd/hub',
                options=chrome_options
            )

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
