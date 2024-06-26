from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

drag_ele = driver.find_element(By.ID, "draggable")
drop_ele = driver.find_element(By.ID, "droppable")
actionChains = ActionChains(driver)
# actionChains.drag_and_drop(drag_ele, drop_ele).perform()
actionChains.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
