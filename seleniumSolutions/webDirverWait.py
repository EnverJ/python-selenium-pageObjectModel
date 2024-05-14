from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://app.hubspot.com/login")
#
# wait = WebDriverWait(driver, 10)
# wait.until(ec.title_is("HubSpot Login and Sign in"))
# print(driver.title)
#
# email_id = wait.until(ec.visibility_of_element_located((By.ID, "username")))
# email_id.send_keys("test@gmail.com")
# driver.find_element(By.ID, "password").send_keys("sdsdsd")

# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
# driver.find_element(By.NAME, "proceed").click()
#
# wait = WebDriverWait(driver, 10)
# alert = wait.until(ec.alert_is_present())
# print(alert.text)
# alert.accept()

# Element TO be clickable

# driver.get("https://app.hubspot.com/login")
# wait = WebDriverWait(driver, 10)
# signup_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Sign up for free")))
# print(signup_link.text)
# signup_link.click()

# present_of_all_elements
driver.get("https://www.freshworks.com/")
wait = WebDriverWait(driver, 10)
link = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "ul > li")))
print(len(link))
for ele in link:
    print(ele.text)
