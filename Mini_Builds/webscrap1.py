from selenium import webdriver
from decouple import config

import time

options = webdriver.options(0)
# driver = webdriver.Firefox('/home/liam/.local/lib/python3.9/site-packages/selenium/webdriver/firerox', firefox_options=options)
driver = webdriver.Firefox(firefox_options=options)

driver.get(config('https://pythonbasics.org/selenium-firefox/'))

button = driver.find_element_by_xpath('/html/body/div/div[1]/div/nav/div[3]/ul/li[2]/a')
time.sleep(2)
