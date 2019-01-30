

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_soup_from_url(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'lxml')


def get_list_from_li_tag(li):

    name = ''
    price = ''
    likes = 0
    img_name = ''

    try:
        name = li.find('dd').find('div', {'class': 'name'}).text.strip()
    except:
        print('name parsing error.. skip..')

    try:
        price = int(li.find('dd').find('div', {'class': 'price-area'})
                    .find('strong', {'class': 'price-value'}).text.replace(',', ''))
    except:
        print('price parsing error.. skip..')

    try:
        likes = int(li.find('dd').find('div', {'class': 'other-info'})
            .find('span', {'class': 'rating-total-count'})
            .text.strip()[1:-1])
    except:
        print('likes parsing error.. set to 0..')

    try:
        full_img_name = li.find('dt').find('img')['src']
        img_name = full_img_name.split('/')[-1]
        download_image_from_coupang('http:' + full_img_name, img_name)
    except:
        print('img parsing error.. skip..')

    return [name, price, likes, img_name]


def download_image_from_coupang(img_url, file_name):
    res = requests.get(img_url)
    with open('./images/' + file_name, 'wb') as f:
        f.write(res.content)

    print('download image to ' + file_name)


def get_product_list_from_li_tag(tag):
    product_list = []  # for 전체 상품 목록

    for li in tag:
        product_list.append(get_list_from_li_tag(li))
    return product_list


def save_to_csv(list_of_list):

    df = pd.DataFrame(list_of_list, columns=['상품명','가격','좋아요','이미지파일'])
    df.to_csv('./data/coupang.csv', index=False, columns=['상품명','가격','좋아요','이미지파일'])

    print('save to ./data/coupang.csv')


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
