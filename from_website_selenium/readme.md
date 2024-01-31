# Selenium 이란.
웹에서 동적으로 로딩되는 컨텐츠를 위해서 주로 사용하지만, 원래는 웹자동화를 위해서 개발된 것으로 이걸 이용해서 UI테스트를 진행하기도 한다. (현업에 있을 떄 이걸 알았더라면, 그놈의 테스트한답시고 주말출근할 일도 없었겠지.) 특징은 '사용자의 행동'을 모방에서 자기 혼자 브라우저를 켜고 로그인을 하고 갖은 일들을 할 수 있다. 

# 공식문서.
[공식문서 - 이걸 진짜 사람이 보라고 만들어 놓은 건지.](https://www.selenium.dev/documentation/)
[한국어자료 - 살짝 라이트한 자료.](https://wikidocs.net/91474)
[한국어자료 - 너무너무 정리가 잘 되어 있음](https://wikidocs.net/177133)

# TODO
- [ ] 스크롤해서 값 가져오기 추가 - 쿠팡 읽어오기
- [ ] 팝업대응하기 - 외국사이트
- [ ] 대기/로딩 처리
- [ ] 스크린샷 찍기
- [ ] 입력, 클릭 등 처리
- [ ] Shadow DOM 이라는 것은?

# Snippet
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "https://huggingface.co/TinyLlama"

# Set options
options = webdriver.ChromeOptions()

# Set service and update latest chrome driver.
service = ChromeService(ChromeDriverManager().install())

# Start browser
response = webdriver.Chrome(service=service, options=options)
response.get(url)
title = response.title

buttons = response.find_elements(By.CSS_SELECTOR, value="#models button")

response.close() # 브라우저 닫기
response.quit() # 아예 selenium 자체를 종료하기

```

# How to
옵션설정
```python
# options.add_argument('--headless') # ensure GUI is off
options.add_experimental_option("detach", True)  # Keeping browser open
options.add_argument("--disable-blink-features=AutomationControlled")  # not robot
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```
요소선택
```python
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```

