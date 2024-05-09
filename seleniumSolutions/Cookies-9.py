from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://amazon.in")

print(driver.get_cookies())

driver.add_cookie({"name": "enver", "domaind": "enverAutomation", "value": "python"})
print(driver.get_cookies())

# cookies = driver.get_cookies()
# for cook in cookies:
#     print(cook)
