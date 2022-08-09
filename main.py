from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://mitey.info/profile')

# Go to sign in screen
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#register-switch > small > a').send_keys(Keys.RETURN)

# Find and enter into username field
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#login-canvas > div > div > form > div:nth-child(1) > div > input').send_keys('nathanielejones@hotmail.com')

# Find and enter password
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#login-canvas > div > div > form > div:nth-child(2) > div > input').send_keys('')

# Find, pause, and select Login button
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#login_button').click()

# find and select Settings
# find and select logout
# close browser
