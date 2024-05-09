from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Setting Chrome options
options = webdriver.ChromeOptions()
options.headless = True  # Enable headless mode
options.add_argument('--incognito')  # Enable incognito mode

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Navigate to the Amazon India webpage
driver.get("https://amazon.in")

# Print the title of the webpage
print(driver.title)

# Optional: Perform more actions here if needed

# Close the driver after the actions are complete
driver.quit()
