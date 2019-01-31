

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')

driver.implicitly_wait(3)

driver.get('http://www.naver.com')

time.sleep(5.0)

driver.close()