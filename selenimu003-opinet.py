

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

def makeDriver():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument('disable-gpu')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    options.add_argument('lang=ko_KR')
    return webdriver.Chrome('./chromedriver.exe', options=options)


def main():

    driver = makeDriver()

    driver.implicitly_wait(3)

    driver.get('http://www.opinet.co.kr/searRgSelect.do')
    time.sleep(3)

    # 시선택 셀렉트박스에서 서울을 선택
    si_select = Select(driver.find_element_by_id('SIDO_NM0'))
    si_select.select_by_index(1)

    # 구선택 셀렉트박스에서 강남구를 선택
    gu_select = Select(driver.find_element_by_id('SIGUNGU_NM0'))
    gu_select.select_by_index(1)

    driver.implicitly_wait(3)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html)

    # soup객체를 통해 데이터 파싱 수행
    # 주유소 기름값 정보를  데이터(list of list)로 확보
    oil_price_list = []
    oil_price_list = parse_oil_price(soup)

    print(oil_price_list)
    driver.close()


def parse_oil_price(soup):

    oil_price_list = []
    for tr in soup.find(id='body1').find_all('tr'):
        try:
            oil_price_list.append(
                [
                    tr.find_all('td')[0].find('a')['href'].split(',')[-12].strip()[1:-1],
                    tr.find_all('td')[0].find('a')['href'].split(',')[-13].strip()[1:-1],
                    tr.find_all('td')[1].text.strip(),
                    tr.find_all('td')[2].find('font').text.strip()
                ]
            )
        except:
            continue
    return oil_price_list


main()