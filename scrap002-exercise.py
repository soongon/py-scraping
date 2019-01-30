

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.coupang.com/np/campaigns/82/components/202952')
soup = BeautifulSoup(res.text, 'html.parser')
# 상품이름  #2575627 > a > dl > dd > div.name
product_title = soup.select_one('#\\32 575627 > a > dl > dd > div.name').text
# 가격
product_price = soup.select_one(
    '#\\32 575627 > a > dl > dd > div.price-area > div:nth-child(1) > div.price > em > strong').text
print(product_title, product_price)