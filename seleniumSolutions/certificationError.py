from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

# # chrome
options = Options()
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

#  The use of desired_capabilities in Selenium has been deprecated.
# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
#                           desired_capabilities=desired_capabilities)
driver.implicitly_wait(10)


driver.get("https://expired.badssl.com/")
time.sleep(5)
