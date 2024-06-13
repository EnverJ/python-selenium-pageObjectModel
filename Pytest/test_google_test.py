import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def init_driver():
    #  executed befor test
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    # executed after tests
    yield driver
    driver.quit()


# def teardown_module(module):
#     driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


def test_google_url(init_driver):
    # assert driver.current_url == "google.com"
    assert "google.com" in driver.current_url
# html report: pytest  Pytest/test_google_test.py -v -s --html=goolge_rest_report.html
