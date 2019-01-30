

import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/Category/NewProduct')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one(
    '#topBooksUl_001 > li:nth-child(1) > div.goods_info > p.goods_name > a')

print(the_tag.text)
