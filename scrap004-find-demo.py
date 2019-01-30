

import requests
from bs4 import BeautifulSoup

res = requests.get('https://music.bugs.co.kr/chart')

soup = BeautifulSoup(res.text, 'lxml')

the_tag = soup\
    .find('div', {'id': 'CHARTrealtime'})\
    .find('tbody').find_all('tr')[0].find('th').find('a')['adultcheckval']

print(the_tag)
