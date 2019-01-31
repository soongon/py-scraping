

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://ko-kr.facebook.com/')

# 아이디와 패스워드 입력창에 아이디와 패스워드를 입력한다.
driver.find_element_by_id('email').send_keys('soongon@gmail.com')
time.sleep(2)
driver.find_element_by_id('pass').send_keys('your_password')
time.sleep(2)

# 로그인 버튼을 클릭한다. (로그인 버튼 아이디가 수시로 변경되어 별도 셀렉터 작성)
driver.find_element_by_css_selector(
    '#login_form > table > tbody > tr:nth-child(2) > ' +
    'td:nth-child(3) > label > input[type="submit"]').click()

time.sleep(3)
driver.close()

