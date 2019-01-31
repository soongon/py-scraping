

import requests

# 헤더를 변경해서 요청

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get('http://www.naver.com', headers=headers)