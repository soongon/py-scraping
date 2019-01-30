

import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'lxml')


def get_list_from_li_tag(li):

    name = ''
    price = ''
    likes = 0

    try:
        name = li.find('dd').find('div', {'class': 'name'}).text.strip()
    except:
        print('name parsing error.. skip..')

    try:
        price = int(li.find('dd').find('div', {'class': 'price-area'}) \
            .find('strong', {'class': 'price-value'}).text.replace(',', ''))
    except:
        print('price parsing error.. skip..')

    try:
        likes = int(li.find('dd').find('div', {'class': 'other-info'}) \
            .find('span', {'class': 'rating-total-count'}) \
            .text.strip()[1:-1])
    except:
        print('likes parsing error.. set to 0..')

    return [name, price, likes]


def get_product_list_from_li_tag(tag):
    product_list = []  # for 전체 상품 목록

    for li in tag:
        product_list.append(get_list_from_li_tag(li))
    return product_list


def save_to_csv(list_of_list):
    print(list_of_list)


def main():

    product_list = []

    for page_num in range(1, 18):
        soup = get_soup_from_url(
            'https://www.coupang.com/np/campaigns/82/components/202952?page='
            + str(page_num))

        li_list = soup.find(id='productList').find_all('li')

        product_list_per_page = get_product_list_from_li_tag(li_list)

        product_list.extend(product_list_per_page)

        print(page_num, '페이지 작업완료...')

    print(len(product_list))

    save_to_csv(product_list)


main()
