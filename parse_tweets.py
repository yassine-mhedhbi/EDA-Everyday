import pandas as pd
import json
from preprocessor import clean as c
import string

tweets = []
with open('data/raw_tweets.txt', 'r') as f:
    for line in f:
        clean = ''
        for ch in c(line):
            if ch not in string.punctuation:
                clean += ch

            if len(clean) > 5:
                tweets.append(clean)

x = list(range(len(tweets)))

df = pd.DataFrame({'id': x,
                   'tweets': tweets})

df.to_csv('tweets.csv', index=False)


