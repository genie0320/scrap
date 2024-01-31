# python Requests
requests는 Python에서 HTTP 요청을 보내는 데 사용되는 라이브러리이다. 다른 웹 사이트로부터 데이터를 가져오거나 API와 상호 작용하기 위해 사용된다. 나는 주로 스크랩할 때 bs4와 함께 페이지 내용을 불러오는데 썼지만, API에서 데이터를 가져오는 것에도 많이 사용하는 모양이다.

# 공식문서
[requests.readthedocs.io](https://requests.readthedocs.io/en/latest/)
# Code snippet
bs4 설치시에는 함꼐 설치되므로 별도로 설치할 필요가 없다.

```python
import requests

url = 'https://example.com'

# url만 줘도 되지만,
# response = requests.get(url)

# header값을 직접 설정할 수도 있다.
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
response = requests.get(url, headers=headers)

html = response.content
print(response.text) 
```

# error solution
한글이 꺠질 때 (사실 이건 bs4에서 해주기도 한다.)
```python
r = requests.get('http://lovflag.tistory.com')
r.encoding	     ### 인코딩 방식 확인
r.encoding = 'utf-8' ### utf-8 인코딩 방식 지정
```
