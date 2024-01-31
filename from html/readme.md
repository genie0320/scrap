<!-- @format -->

# html에서 직접 추출해내기
beautifulSoup4는 비록 공식문서는 엉망이지만(보기 좋은 개발문서의 중요성!) 간단하게 사용하기 좋은 웹컨텐츠 추출기(적어도 현재의 나에게는)이다. 대개 selenium과 동시에 익히는 경우가 많고, 메서드명이 비슷하여 그 차이를 확실히 차이를 기억해둘 필요가 있다. 

# 공식문서
[BeautifulSoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[BeautifulSoup4 readthedocs.io-조금 더 읽기 쉽다.](https://beautiful-soup-4.readthedocs.io/en/latest/)

# ToDos
- [ ] bs4 함수명 정리
- [ ] pip install lxml > 활용방법
- [ ] prettify() > 사용방법
- [ ] 정규표현식 사용방법
- [ ] bs4와 selenium 객체 호환방법 찾기

# Getting Started
```python
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

```
# 많이 쓰는 구문 정리
```python
# 텍스트 추출
print(soup.get_text())

# 링크 추출
for link in soup.find_all('a'):
    print(link.get('href'))
```
```python
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

## 속성만지기
```python
tag.attrs 
# {'id': 'boldest'}

tag.attrs.keys()
# dict_keys(['id'])
```
