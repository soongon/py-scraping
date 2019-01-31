

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)

driver.get('http://www.opinet.co.kr/searRgSelect.do')
time.sleep(3)

gu_select = Select(driver.find_element_by_id('SIGUNGU_NM0'))
gu_select.select_by_index(8)

time.sleep(3)

driver.close()