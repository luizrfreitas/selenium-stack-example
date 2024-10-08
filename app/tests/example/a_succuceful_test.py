import common_test.py

def test_example(browser):
    # Example test case
    url = "http://google.com"

    # Perform a GET request to verify the site is up
    response = requests.get(url)
    assert response.status_code == 200  # Check the HTTP response status

    # Navigate to the URL using Selenium
    browser.get(url)

    # Check the title of the page
    assert "Google" in browser.title
