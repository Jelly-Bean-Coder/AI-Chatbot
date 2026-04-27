import requests
from bs4 import BeautifulSoup

links = []
text = ""

headers = {
    'User-Agent': 'MyCoolScraper/1.0 (im0947362@gmail.com)'
}

with open("websites.txt", "r") as file:
    for line in file.readlines():
        links.append(line.strip())
        print(line)

for link in links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    text += "\n\n" + str(soup.get_text().strip())

print(text)