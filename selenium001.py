

from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver.exe')

browser.implicitly_wait(3)

browser.get('http://www.naver.com')

time.sleep(5.0)

browser.close()