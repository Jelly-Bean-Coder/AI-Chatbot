import requests, urllib
from bs4 import BeautifulSoup

links = []
nested_links = [] # Will change fo each source visited
first = True
with open("info.txt", "w"): pass

with open("websites.txt", "r") as file:
    for line in file.readlines():
        links.append(line.strip())

def scrape(url):
    global first
    headers = {
        'User-Agent': 'MyCoolScraper/1.0 (im0947362@gmail.com)',
        'Accept': 'text/*',
        'Accept-Language': 'en-CA',
        'Connection': 'keep-alive',
    }




    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    with open("info.txt", "a", encoding="utf-8") as file:
        if first:
            first = False
            file.write("==ARTICLE-START==\n\n")

        else:
            file.write("\n==ARTICLE-START==\n\n")

        text = str(soup.get_text())
        text = "\n".join(line for line in text.splitlines() if line.strip())
        file.write(text)
        file.write("\n\n==ARTICLE-END==\n")

    local_nested_links = []
    for tag in soup.find_all("a"):
        local_nested_links.append(requests.compat.urljoin(url, tag.get("href")))

    return local_nested_links

def check_root(pre_url, new_url):
    def split(link):
        splitted_link = urllib.parse.urlsplit(link)
        root = f"{splitted_link.scheme}://{splitted_link.netloc}"
        return root

    if split(pre_url) == split(new_url):
        return True
    else:
        return False


max_depth = 4
links_visited = set()
def recursive_scrape(link, max_depth, current_depth=0):
    # Check if link is scraped twice
    if current_depth >= max_depth: return
    if link in links_visited: return
    else:
        links_visited.add(link)
        new_urls = scrape(link)
        current_depth += 1
        for url in new_urls:
            if check_root(url, link):
                recursive_scrape(url, max_depth, current_depth)




