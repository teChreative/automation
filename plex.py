from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# 1 - go to plex.tv
# 2 - enter username
# 3 - enter password
# 4 - hover over OPEN PLEX
# 5 - select OPEN PLEX
# 6 - select Movies in menu
# 7 - enter movie name in search field (star wars - maybe from user input)
# 8 - hover and select movie choice
# 9 - select PLAY button
