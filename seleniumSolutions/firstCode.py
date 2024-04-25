import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://google.com")
driver.find_element(By.NAME, "q").send_keys("Naveen Automationlabs youtube")
# optionsLists = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e  li div.eIPGRd div.pcTkSc div.lnnVSe div.wM6W7d span")
optionsLists = driver.find_elements(By.CSS_SELECTOR, ".G43f7e .wM6W7d span")
print(optionsLists)
for ele in optionsLists:
    print(ele.text)
    if ele.text == "naveen automationlabs youtube core java":
        ele.click()
        break

time.sleep(3)

print(driver.title)

driver.quit()
