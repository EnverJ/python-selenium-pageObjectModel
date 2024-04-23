import selenium
from selenium.webdriver.chromium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestData:
    # chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    BASE_URL = "https://app.hubspot.com/login"
    USER_NAME = "xxxxx@gmail.com"
    PASSWRD = "Selenium@00"
    LOGIN_PAGE_TITLE = "HubSpot Login and Sign in"
    HOME_PAGE_TITLE = "User Guide | HubSpot"
    HOME_PAGE_HEADER1 = "User Guides"
    HOME_PAGE_HEADER3 = "Recommended: All you need to get started"
