from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')

# Go to sign in screen
# Find and enter into username field
# Find and enter password
# Find, pause, and select Login button
# find and select Settings
# find and select logout
