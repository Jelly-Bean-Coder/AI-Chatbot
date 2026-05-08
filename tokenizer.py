import nltk
import typing
import numpy as np
import datetime
import json


nltk.download("punkt_tab")

start_token = "==ARTICLE-START=="
end_token = "==ARTICLE-END=="


def separate_sources(file: typing.IO):
    separated_sources = []
    with open(file, "r", encoding="utf-8") as file:
        current_string = ""
        text = file.readlines()
        appending = False

        for item in text:
            new_item = item.strip()

            if new_item == start_token:
                appending = True

            elif new_item == end_token:
                separated_sources.append(current_string)
                appending = False
                current_string = ""

            if appending and new_item != start_token:
                current_string += " " + str(item.strip())

    return separated_sources

def tokenize(text):
    stemmer = nltk.stem.snowball.SnowballStemmer("english")
    grand_stemmed = []
    for source in text:
        article_stemmed = []
        words = nltk.word_tokenize(source)
        for word in words:
            article_stemmed.append(stemmer.stem(word))

        grand_stemmed.append(article_stemmed)

    return grand_stemmed

def flatten(items):
    flattened = []
    for item in items:
        if isinstance(item, list):
            flattened.extend(flatten(item))

        else:
            flattened.append(item)

    return flattened

def create_matrix():
    separated_sources = separate_sources(file="info.txt")
    tokens = tokenize(separated_sources)

    map = sorted(set(flatten(tokens)))
    data = np.zeros((len(separated_sources), len(map)), dtype="float32")

    for article, article_content in enumerate(tokens):
        for word in article_content:
            if word in map:
                data[article, map.index(word)] = 1.0

    update_files(map, data, separated_sources)
    return (map, data, separated_sources)



def update_files(map, data, separated_sources):
    knowlege = {
        "map": map,
        "last-updated": datetime.datetime.now().date().isoformat(),
        "article-count": len(separated_sources)
    }
    with open("knowledge.json", "w", encoding="utf-8") as file:
        json.dump(knowlege, file)

    np.save("brain.npy", data)



