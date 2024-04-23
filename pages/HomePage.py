from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER5 = (By.XPATH, "//i18n-string[normalize-space()='Your Sales tools progress']")
    HEADER1 = (By.CSS_SELECTOR, "h1.private-header__heading private-header__heading--solo")
    HEADER3 = (By.XPATH, "//h3[normalize-space()='Recommended: All you need to get started']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_sales_header_exist(self):
        return self.is_visible(self.HEADER5)

    def get_private_header1(self):
        if self.is_visible(self.HEADER1):
            return self.do_element_text(self.HEADER1)

    def get_recommended_header(self):
        if self.is_visible(self.HEADER3):
            return self.do_element_text(self.HEADER3)
