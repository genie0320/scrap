# !pip install --quiet bs4 selenium webdriver-manager
# !pip install --quiet icecream

import requests
from bs4 import BeautifulSoup as bs4
from bs4 import SoupStrainer as strainer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from icecream import ic

# get list of tinyllama versions from huggingface.
url = "https://python.langchain.com/docs/get_started/introduction"

# 일단 requests 로 간보기
response = requests.get(url)
if response.status_code == 200:
    print("Activate Requests **************************")
    soup = bs4(response.text, "html.parser")
    title = soup.title.text
else:
    print("Activate Selenium **************************")
    # Set options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # ensure GUI is off
    # options.add_experimental_option("detach", True) # Keeping browser open
    options.add_argument("--disable-blink-features=AutomationControlled")  # not robot
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set service and update latest chrome driver.
    service = ChromeService(ChromeDriverManager().install())

    # Start browser
    response = webdriver.Chrome(service=service, options=options)
    response.get(url)
    title = response.title

ic(title)

# buttons = response.find_elements(By.CSS_SELECTOR, value='#models button')

# # Locator로 바로 특정 텍스트를 포함하는 버튼을 찾을 수가 없어서 반복문 사용.
# for btn in buttons:
#   if btn.text.startswith("Expand"):
#     button.click()
#   break

# models = response.find_element(by=By.ID, value="models")

# # models = bs4(response.text, 'html.parser', parse_only=strainer("div", id = 'models'))
# for model in models.find_elements(By.TAG_NAME,value='h4'):
#   print(model.text.strip())
