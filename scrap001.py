

# requests --> http client, 웹 페이지를 가져오는 역할
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')

# bs4 사용 데이터 파싱
soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#KOSPI_now')

print(the_tag.text)

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a





