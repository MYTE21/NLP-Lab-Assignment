import re
import pandas as pd


def dataset_load():
    data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")
    return data["English"], data["Bangla"]


def corpus_size_words():
    return 0


def corpus_size_lines():
    return 0


def corpus_size_chars():
    return 0


def avg_sen_len():
    return 0


def vocabulary_size():
    return 0


def lex_div():
    return 0


if __name__ == "__main__":
    eng_data, ban_data = dataset_load()