

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.coupang.com/np/campaigns/82/components/202952')
soup = BeautifulSoup(res.text, 'lxml')

li_list = soup.find(id='productList').find_all('li')

product_list = [] # for 전체 상품 목록

for li in li_list:
    product_list.append(
        [li.find('dd').find('div', {'class': 'name'}).text.strip(),
         int(li.find('dd').find('div', {'class': 'price-area'})\
            .find('strong', {'class': 'price-value'}).text.replace(',', '')),
         li.find('dd').find('div', {'class': 'other-info'})\
            .find('span', {'class': 'rating-total-count'}).text.strip()]
    )

print(product_list)
