from collections import Counter
import nltk
from nltk.corpus import stopwords
import string




filename = "Роман «Анна Каренина».txt"


def stop_words():
    stop_words = []
    with open("stop_words.txt", "r", encoding="utf=8") as file:
        for words in file:
            all_words = words.split("\n")
            for word in all_words:
                stop_words.append(word)
    return stop_words


def load_text(filename):
    all_text = ""
    try:
        with open(filename, "r", encoding="utf=8") as f:
            for text in f:
                all_text += text
        return all_text
    except FileNotFoundError:
        print("Файл не найден!")
        return None


def clean_text(text):
    custom_stopwords = stopwords.words('russian') + stop_words()
    words = text.split(" ")
    cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in custom_stopwords]
    return cleaned_words


def count_words(cleaned_words):
    word_counts = Counter(cleaned_words)
    return word_counts


def display_top_words(word_counts, n=10):
    top_words = word_counts.most_common(n)
    print("Самые часто встречающиеся слова в романе:")
    for word, count in top_words:
        print(f"{word}: {count}")


cleaned_words = clean_text(load_text(filename))
word_counts = count_words(cleaned_words)
display_top_words(word_counts)