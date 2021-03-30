import re
import pandas as pd


data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")

text = data["Bangla"]
# print(text)
sentences = text[4285]
print("Pre. Sen : ", sentences)
sentences = re.split(r'[!?.।]+ +', sentences)
print("Sen : ", sentences)
print(len(sentences))
a = []
a.append(sentences)
print(len(a))

# for stuff in sentences:
    # print(stuff) 4293 4285 "Can I help you? ""No, thank you. I'm just looking around."""