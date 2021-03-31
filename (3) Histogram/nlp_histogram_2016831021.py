import pandas as pd
import string
import re


def dataset_load():
    data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")
    return data["English"], data["Bangla"]


def corpus_size_words(data):
    size = 0
    for single_data in data:
        size += len(re.split('[; |,]+', single_data))
    return size


def corpus_size_lines(data):
    size = 0
    for single_data in data:
        sentences = re.split(r'[!?.।]+ +', single_data)
        size += len(sentences)
    return size


def corpus_size_chars(data):
    size = 0
    for single_data in data:
        size += len(single_data)-single_data.count(" ")
    return size


def avg_sen_len(total_words, total_sentences):
    return total_words/total_sentences


def vocabulary_size():
    return 0


def lex_div():
    return 0


if __name__ == "__main__":
    eng_data, ban_data = dataset_load()
    print(avg_sen_len(corpus_size_words(eng_data), corpus_size_lines(eng_data)))
