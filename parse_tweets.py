import pandas as pd
import json
from preprocessor import clean as c


tweets = []
with open('data/test.txt', 'r') as f:
    for line in f:
        tweets.append(json.loads(line))


df = pd.DataFrame(tweets, columns=tweets[0].keys())
df = df[['id', 'text']]
df['text'] = df['text'].map(c)

df.to_csv('data/tweets.csv', index=False)
