from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# 1 - go to plex.tv
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.plex.tv/')

driver.find_element(
    By.CSS_SELECTOR, '#universal-search-input').send_keys('star wars')

time.sleep(2)
# hoverSTARWARS = ActionChains(driver)
# SW = driver.find_element(
#     By.CSS_SELECTOR, '#universal-search-item-0')
# hoverSTARWARS.move_to_element(SW).perform()

# hoverSTARWARS = ActionChains(driver)
# SW = driver.find_element(By.LINK_TEXT, 'Star Wars')
# hoverSTARWARS.move_to_element(SW).perform()

driver.find_element(
    By.CSS_SELECTOR, '#universal-search-menu > div')

driver.find_element(
    By.CSS_SELECTOR, '#universal-search-menu > div > div')

driver.find_element(
    By.CSS_SELECTOR, '#universal-search-menu > div > div > div')

myList = driver.find_element(
    By.CSS_SELECTOR, '#universal-search-menu > div > div > div > div:nth-child(2)')

for movie in myList:
    print(movie.text)
    if movie.text == "Star Wars":
        movie.click()
        break

"""
# 2 - find and click burger
driver.find_element(
    By.CSS_SELECTOR, '#plex-global-nav > header > div.fresnel-lessThan-md.nav.menuContainer > button').send_keys(Keys.RETURN)

# 3 - click SIGN IN
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#plex-global-nav > header > div.mobile-navbar.chroma_Modal_module_backdrop.animate__animated.animate__fadeIn > div.chroma_Modal_module_modal.chroma_Modal_module_s.chroma_Modal_module_modal > div > div.chroma_Scroller_modules_scroller.chroma_Scroller_modules_vertical.chroma_Scroller_modules_auto > span > div > div.signup.chroma_Flex_module_flex.chroma_Flex_module_horizontal.chroma_Flex_module_shrink.chroma_Flex_module_nativeGap.chroma_Flex_module_m.mobile-nav-group > a.signin.chroma_Button_module_button.chroma_UnstyledButton_module_unstyledButton.chroma_shared_module_base.chroma_Button_module_default.chroma_Button_module_m').send_keys(Keys.RETURN)

# 4 - enter username into field
time.sleep(2)
driver.find_element(
    By.NAME, 'email').send_keys('boog')

# 3 - enter password into field
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password')

# 4 - hover over OPEN PLEX button
time.sleep(2)
hoverOPENPLEX = ActionChains(driver)
OP = driver.find_element(
    By.CSS_SELECTOR, '')
hoverOPENPLEX.move_to_element(OP).perform()

# 5 - select OPEN PLEX button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 6 - select Movies link in menu
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)

# 7 - enter movie name in search field (star wars - maybe from user input)


# 8 - hover and select movie choice
time.sleep(2)
hoverSELECTMOVIE = ActionChains(driver)
SM = driver.find_element(
    By.CSS_SELECTOR, '')
hoverSELECTMOVIE.move_to_element(SM).perform()

# 9 - select PLAY button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '').send_keys(Keys.RETURN)"""
