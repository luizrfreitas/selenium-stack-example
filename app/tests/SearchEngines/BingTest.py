from ..CommonTestCase import CommonTestCase


class BingTest(CommonTestCase):

    def test_bing_search(self):
        self.driver.get("https://www.bing.com/")
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Selenium Grid")
        search_box.submit()
        self.assertIn("Selenium Grid", self.driver.title)
