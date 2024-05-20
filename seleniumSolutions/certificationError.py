from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService



options = Options()
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),options=options))
driver.implicitly_wait(10)

driver.get("https://expired.badssl.com/")
time.sleep(5)
