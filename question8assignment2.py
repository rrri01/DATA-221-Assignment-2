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
# headings = soup.find("h2")
# print(headings.string)

with open("headings.csv", mode="w", newline="") as f:
    writer = csv.writer(f)

    for heading in soup.body.find_all("h2"):
        if "References" in heading.string:
            continue
        if "External links" in heading.string:
            continue
        if "See also" in heading.string:
            continue
        if "Notes" in heading.string:
            continue
        writer.writerow(heading)


