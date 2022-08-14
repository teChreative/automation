from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# 1 - go to plex.tv
driver = webdriver.Chrome()
driver.get('https://www.plex.tv/')

# 2 - enter username into field
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 3 - enter password into field
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 4 - hover over OPEN PLEX button
time.sleep(2)
a = ActionChains(driver)
m = driver.find_element(
    By.CSS_SELECTOR, '')
a.move_to_element(m).perform()

# 5 - select OPEN PLEX button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 6 - select Movies link in menu
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 7 - enter movie name in search field (star wars - maybe from user input)


# 8 - hover and select movie choice
time.sleep(2)
a = ActionChains(driver)
m = driver.find_element(
    By.CSS_SELECTOR, '')
a.move_to_element(m).perform()

# 9 - select PLAY button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)
