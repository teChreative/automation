from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://mitey.info/profile')

# Go to sign in screen
time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, '#register-switch > small > a').send_keys(Keys.RETURN)

# Find and enter into username field
time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, '#login-canvas > div > div > form > div:nth-child(1) > div > input').send_keys('')

# Find and enter password
time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, '#login-canvas > div > div > form > div:nth-child(2) > div > input').send_keys('')

# Find, pause, and select Login button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#login_button').click()

# find and select Settings https://www.tutorialspoint.com/how-can-i-perform-mouse-hover-action-in-selenium-python
time.sleep(2)
a = ActionChains(driver)
m = driver.find_element(
    By.CSS_SELECTOR, '#privateNavbar > div.topnav-right > div:nth-child(5)')
a.move_to_element(m).perform()

# find and select logout
time.sleep(2)
b = ActionChains(driver)
n = driver.find_element(By.CSS_SELECTOR, '#logout-button')
b.move_to_element(n).perform()
time.sleep(2)
n.click()

# log me out Yes/No
# Automated YES -
time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > button.confirm').click()
# Automated NO -
# driver.find_element(By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > button.cancel').click()

# OK After Automated YES
time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > button.confirm').click()

# close browser
driver.close()
