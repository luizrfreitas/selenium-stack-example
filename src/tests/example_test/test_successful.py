from tests.SeleniumCommon import SeleniumCommon

class TestSuccessful(SeleniumCommon):

    def test_google(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title
