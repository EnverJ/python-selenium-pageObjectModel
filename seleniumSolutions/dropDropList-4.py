from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


def select_value_from_dropdown(dropDownOptionList, value):
    print(dropDownOptionList)
    for ele in dropDownOptionList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


country_options = driver.find_elements(By.XPATH, "//select[@id='Form_getForm_Country']/option")
select_value_from_dropdown(country_options, "Jamaica")
time.sleep(10)

country_dropDown = driver.find_element(By.XPATH, "//select[@id='Form_getForm_Country']")
select_values(country_dropDown, "Angola")
time.sleep(10)
