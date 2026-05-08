# Custom NumPy Chatbot 🤖
A "from-scratch" AI chatbot built in Python that learns from web-scraped data and text files. This project avoids heavy libraries like TensorFlow or PyTorch to focus on the underlying linear algebra and Natural Language Processing (NLP) logic.

## 🚀 Overview
This chatbot uses a Neural Network built entirely on NumPy. It processes human language through a custom pipeline and updates its internal weight matrices based on new information added to its training database.

## Core Features
 - Custom Tokenization: Uses NLTK for professional-grade text splitting and stemming.

 - __Manual Training Pipeline__: I manually curate articles on aviation, finance, and physics to "feed" the brain.

 - __NumPy Brain__: A multi-layer perceptron (MLP) architecture using matrix multiplication and backpropagation.

 - __Incremental Learning__: The model is designed to be updated over time as new data is appended to the master text file.

## 🛠️ Tech Stack
 - __Language__: Python 3.14

 - __Math__: NumPy (Linear Algebra & Matrix Operations)

 - __NLP__: NLTK (Natural Language Toolkit)

 - __Data Handling__: JSON (for Vocabulary) and .npy (for Weight persistence)

 - __IDE__: PyCharm