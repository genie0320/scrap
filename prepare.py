import requests

# 아래 두줄은 거의 상용코드. 걍 외우자.
res = requests.get("http://www.google.com")  # 스크래핑대상
# 가능여부 타진. status_code가 200 이외라면 에러내고 이후 진행 안함.
res.raise_for_status()

print(len(res.text))


def create_reult(text):
    with open("./temp/test_result.html", "w", encoding="UTF8") as f:
        f.write(text)


create_reult(res.text)
