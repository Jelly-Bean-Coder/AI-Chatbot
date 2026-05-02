import requests
from bs4 import BeautifulSoup

links = []

headers = {
    'User-Agent': 'MyCoolScraper/1.0 (im0947362@gmail.com)'
}

with open("websites.txt", "r") as file:
    for line in file.readlines():
        links.append(line.strip())

for link in links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    first = True
    with open("info.txt", "w", encoding="utf-8") as file:
        if first:
            first = False
            file.write("==ARTICLE-START==\n\n")

        else:
            file.write("\n==ARTICLE-START==\n\n")

        text = str(soup.get_text())
        text = "\n".join(line for line in text.splitlines() if line.strip())
        file.write(text)
        file.write("\n\n==ARTICLE-END==\n")