from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/")

# go to bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# go to top
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

# NestedFrames = driver.find_element(By.LINK_TEXT, "Nested Frames")
# driver.execute_script("arguments[0].scrollIntoView(true)", NestedFrames)
#
# JQuery = driver.find_element(By.LINK_TEXT, "JQuery UI Menus")
# driver.execute_script("arguments[0].style.border = '3px solid red'", JQuery)
# time.sleep(3)
# driver.execute_script("arguments[0].click();", JQuery)
# title = driver.execute_script("return document.title;")
# print(title)
# driver.execute_script("history.go(0);")
# # driver.execute_script("alert('hello enver!!!!!!!!')")

# inner_text = driver.execute_script('return document.documentElement.innerText')
# print(inner_text)
#
# print(driver.execute_script("return navigator.userAgent "))

inputs = driver.find_element(By.LINK_TEXT, "Inputs")
driver.execute_script("arguments[0].click();", inputs)
# vv = "document.getElementsByClassName('document.querySelector("  # content > div > div > div > input[type=number]")').value="enver"
# driver.execute_script(vv)
