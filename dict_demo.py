

movies = {
    '봉준호': '괴물',
    '박훈정': '신세계',
    '우민호': '내부자들'
}

# C
movies['강우석'] = '친구'
print(movies)

# R
#print(movies['박훈'])
print(movies.get('박훈'))

# U
movies['박훈정'] = '마약왕'
print(movies)

# D
del movies['박훈정']
print(movies)

article = {
    'number': 4,
    'title': 'slkdfjlskdjflksdjflkdsjfklsd',
    'author': 'kim',
    'likes': 35,
    'content': 'sldkfjlksdjflksdjfklsdjfslkfj0',
    'replys': [
        {'author': 'lee', 'content': 'hello'},
        {'author': 'park', 'content': 'I hate you'},
        {'author': 'choi', 'content': 'I like you'}
    ]
}

if article.get('titl'):
    print('titl 키가 있어요')
else:
    print('없어요')

