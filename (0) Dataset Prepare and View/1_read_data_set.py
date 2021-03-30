import pandas as pd


if __name__ == '__main__':
    data = pd.read_csv("../Datasets/(1) Main Datasets/ben.txt", sep="\t", header=None, names=["English", "Bangla", "Attribution"])
    print(data.head())
