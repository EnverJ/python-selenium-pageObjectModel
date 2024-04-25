from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
print(driver.title)

driver.find_element(By.CSS_SELECTOR,"#username").send_keys("xxx@gmail.com")
driver.find_element(By.ID,"password").send_keys("fdfdf")

time.sleep(10)
