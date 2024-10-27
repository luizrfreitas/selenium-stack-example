from ..CommonTestCase import CommonTestCase


class DuckDuckGoTest(CommonTestCase):

    def test_duck_duck_go_search(self):
        self.driver.get("https://duckduckgo.com/")
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Selenium Grid")
        search_box.submit()
        self.assertIn("Selenium Grid", self.driver.title)
