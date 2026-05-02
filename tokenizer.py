import nltk
import typing

nltk.download("punkt_tab")

separated_sources = []
start_token = "==ARTICLE-START=="
end_token = "==ARTICLE-END=="


def separate_sources(file: typing.IO):
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

def tokenize(text):
    stemmer = nltk.stem.snowball.SnowballStemmer("english")
    stemmed = []
    for source in text:
        words = nltk.word_tokenize(source)
        for word in words:
            stemmed.append(stemmer.stem(word))
    print(stemmed)

def main(file_path: str):
    separate_sources(file_path)
    tokenize(separated_sources)

main("info.txt")