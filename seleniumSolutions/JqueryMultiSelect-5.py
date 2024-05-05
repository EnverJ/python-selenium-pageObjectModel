from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
import time


def select_value(option_list, value):
    if not value[0] == "all":
        for ele in option_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in option_list:
                ele.click()
        except Exception as e:
            print(e)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

justAnInputBox = driver.find_element(By.XPATH, "//input[@id='justAnInputBox']")
justAnInputBox.click()
time.sleep(5)

drop_list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
# value_list = ["choice 2", "choice 3", "choice 2 3"]
value_list = ["all"]
select_value(drop_list, value_list)
# select_value(drop_list, "choice 2")
# select_value(drop_list, "choice 3")
# select_value(drop_list, "choice 2 3")
# for ele in drop_list:
#     print(ele.text)
#     if ele.text =="choice 2":
#         ele.click()
#         break
