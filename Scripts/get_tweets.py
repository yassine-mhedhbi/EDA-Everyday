import tweepy
import json


class Covid19Listener(tweepy.StreamListener):

    def __init__(self, tweets, f):
        super().__init__()
        self.num = tweets
        self.n = 0
        self.file = open(f, 'w')

    def on_status(self, status):
        js = status._json
        t = status.text
        if js['lang'] == 'en':
            self.file.write(t + '\n')
            self.n += 1
            if self.n < self.num:
                return True
            else:
                return False
                self.file.close()


        def on_error(self, status):
            print(status)


with open('apis.json') as js:
    keys = json.load(js)

access_token = keys['access token']
access_token_secret = keys['access secret']
consumer_key = keys['consumer key']
consumer_secret = keys['consumer secret']

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

spy = Covid19Listener(1000000, 'data/raw_tweets.txt')
stream = tweepy.Stream(auth, spy)
stream.filter(track=['corona', 'covid19', 'coronavirus', 'corona virus', 'lockdown'])
