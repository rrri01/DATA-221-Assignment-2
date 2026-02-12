
import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
}

contents = requests.get(url, headers=headers)
soup = BeautifulSoup(contents.text, "html.parser")

row_data = []

div = soup.find("div", id = "mw-content-text")
for table in div.find_all("table"):
    for table_row in table.find_all("tr"):
        for table_data in table_row.find_all("td"):
            for i in table_data.find_all("li"):
                row_data.append(i.text)

with open("wiki_table.csv", mode="w", newline="") as f:
    writer = csv.writer(f)

    for title in row_data:
        writer.writerow(title)












