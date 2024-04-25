from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

username_url = driver.find_element(By.ID, "Form_getForm_subdomain")
full_name = driver.find_element(By.ID, "Form_getForm_Name")
businessEmail = driver.find_element(By.ID, "Form_getForm_Email")

solutionsLink = driver.find_element(By.LINK_TEXT, "Solutions")
username_url.send_keys("Week Automation")
full_name.send_keys("Week Automaton lab")
businessEmail.send_keys("xxxx.gmail.com")
solutionsLink.click()
time.sleep(2)
