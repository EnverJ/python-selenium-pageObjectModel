from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
# driver.get("http://amazon.in")
# driver.get_screenshot_as_file("amazon.png")

'''full screenshot need to be executed in headless mode'''

options = webdriver.ChromeOptions()
options.headless = True  # Enable headless mode
options.add_argument('--incognito')  # Enable incognito mode

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Navigate to the Amazon India webpage
driver.get("https://amazon.in")

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S("Width"), S("Height"))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png');
