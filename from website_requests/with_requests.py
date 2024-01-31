# !pip install bs4
# !pip install icecream

import requests
from bs4 import BeautifulSoup as bs4
from bs4 import SoupStrainer as strainer

from icecream import ic

# get list of tinyllama versions from huggingface.
url = "https://huggingface.co/TinyLlama"
response = requests.get(url)

models = bs4(response.text, "html.parser", parse_only=strainer("div", id="models"))

for model in models.select("h4"):
    print(model.text.strip())
