import numpy as np

import tokenizer
import web_scraper

links = []

with open("websites.txt", "r") as file:
    for line in file.readlines():
        links.append(line.strip())

for link in links:
    web_scraper.recursive_scrape(link, max_depth=2)

map_data_separate_sources = tokenizer.create_matrix()

map = map_data_separate_sources[0]
separate_sources = map_data_separate_sources[2]

array = np.zeros((len(map)))

while True:
    index = 0
    prompt = input("AI: What's on your mind? ")
    words = tokenizer.tokenize(prompt)
    tmp = None
    for word_index, word in enumerate(words):
        if word in map:
            index = map.index(word)

        array[index] = 1.0
        scores = np.dot(np.load("brain.npy"), array)
        tmp = np.argmax(scores)
    print(separate_sources[tmp])



