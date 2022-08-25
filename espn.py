from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - go to ESPN
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.espn.com/')

# 2 - hover over bar
# driver.find_element(
#     By.CSS_SELECTOR, '#global-nav > ul').send_keys(Keys.RETURN)
time.sleep(2)

# hoverDOTS = ActionChains(driver)
# DT = driver.find_element(
#     By.CSS_SELECTOR, '#global-nav > ul')
# hoverDOTS.move_to_element(DT).perform()

# select three dot
driver.find_element(
    By.CSS_SELECTOR, '#main-container > div > section.col-one > article:nth-child(1) > div > ul > li.quicklinks_list__item.quicklinks_list__item--eplus-paywall > a').send_keys(Keys.RETURN)
time.sleep(2)

# 3 - select sport - BOXING
driver.find_element(
    By.CSS_SELECTOR, '#global-nav > ul > li.none.more.hover > div > ul > li.sports.menu-boxing > a').send_keys(Keys.RETURN)
time.sleep(2)


# driver.find_element(
#     By.CSS_SELECTOR, '').send_keys('')
# time.sleep(2)
