# for this question, i just referred to some old code from a cpsc 217 project to remember all the key words to use

import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
}

contents = requests.get(url, headers=headers)
soup = BeautifulSoup(contents.text, "html.parser")
title = soup.find("title")
print(title.string)

container = soup.find("div", attrs={"id": "mw-content-text"})
para = container.find_all("p")
print(para[1].text)
