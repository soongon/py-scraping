

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.coupang.com/np/campaigns/82/components/202952')
soup = BeautifulSoup(res.text, 'html.parser')

product_list = soup.select('#productList > li')

for li in product_list:
    print(li)
    print('------------------------------------------')



#goodsList > ul > li:nth-child(1) > a > div.plp-info-subscription > div.title