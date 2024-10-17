from CommonTestCase import CommonTestCase


class SuccessefulTest(CommonTestCase):

    def test_google_search(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Selenium Grid")
        search_box.submit()
        self.assertIn("Selenium Grid", self.driver.title)
