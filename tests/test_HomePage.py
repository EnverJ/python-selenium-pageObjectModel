from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWRD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWRD)
        header = homePage.get_private_header1()
        assert header == TestData.HOME_PAGE_HEADER1

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWRD)
        header3 = homePage.get_recommended_header()
        assert header3 == TestData.HOME_PAGE_HEADER3

    def test_home_page_setting(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWRD)
        assert homePage.is_sales_header_exist()
