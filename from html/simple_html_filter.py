import requests
from bs4 import BeautifulSoup as bs4
from bs4 import SoupStrainer as strainer

# gat things from html
htmls = """
  Paste html code here then run
"""

# gat things from file
# with open("index.html") as fp:
#     soup = bs4(fp, 'html.parser')

models = bs4(htmls, "html.parser", parse_only=strainer("div", id="models"))

for model in models.select("h4"):
    print(model.text.strip())
