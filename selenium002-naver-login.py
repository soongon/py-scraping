

from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)

driver.get('https://ko-kr.facebook.com/')

# 아이디와 패스워드 입력창에 아이디와 패스워드를 입력한다.
driver.find_element_by_id('email').send_keys('soongon@gmail.com')
time.sleep(2)
driver.find_element_by_id('pass').send_keys('password')
time.sleep(2)

# 로그인 버튼을 클릭한다. (로그인 버튼 아이디가 수시로 변경되어 별도 셀렉터 작성)
driver.find_element_by_css_selector(
    '#login_form > table > tbody > tr:nth-child(2) > ' +
    'td:nth-child(3) > label > input[type="submit"]').click()

time.sleep(1)

driver.get('https://www.facebook.com/find-friends/browser/')
driver.get_screenshot_as_file('test.png')
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

driver.close()

print(soup)