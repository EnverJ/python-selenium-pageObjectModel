from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

'''Right Click'''
right_Click_ele = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
act_chain = ActionChains(driver)
act_chain.context_click(right_Click_ele).perform()

right_click_options = driver.find_elements(By.XPATH, "/html/body/ul/li")
for ele in right_click_options:
    print(ele.text)
    if ele.text == "Copy":
        ele.click()
        break
