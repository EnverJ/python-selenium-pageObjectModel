import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope="class")
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_test:
    pass


class Test_Google_Chrome(Base_Chrome_test):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
