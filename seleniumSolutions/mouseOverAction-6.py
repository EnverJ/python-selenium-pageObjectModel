from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://corporate.spicejet.com/spicelock.aspx")

'''mover to Element'''

login_ele = driver.find_element(By.ID, "ctl00_HyperLinkLogin")
act_chains = ActionChains(driver)

act_chains.move_to_element(login_ele).perform()

travelAgent = driver.find_element(By.LINK_TEXT, "Travel Agent Login")
travelAgent.click()
