from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Go to ESPN
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.espn.com/')

time.sleep(2)

# 2 - Select from menu
# THREE DOTS - #global-nav > ul > li.none.more > a
# TENNIS - #global-nav > ul > li.sports.menu-tennis > a
driver.find_element(
    By.CSS_SELECTOR, '#global-nav > ul > li.none.more > a').send_keys(Keys.RETURN)
time.sleep(2)

# 3 - Select sport
# BOXING - #global-nav > ul > li.none.more.hover > div > ul > li.sports.menu-boxing > a
# TENNIS - #global-nav > ul > li.sports.menu-tennis.hover > div > ul > li:nth-child(1) > a
driver.find_element(
    By.CSS_SELECTOR, '#global-nav > ul > li.none.more.hover > div > ul > li.sports.menu-boxing > a').send_keys(Keys.RETURN)
time.sleep(3)

# 4 - close browser
driver.close()
