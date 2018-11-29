import tweepy
import json
import nltk
from tweepy import OAuthHandler
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')


def process_or_store():
    consumer_key = '4IjEmWFE289MmeIqjcY5WBqow'
    consumer_secret = 'PXNBzRcPNdEIygVl6C5eBH8r6hKPpLDmzff3Hil4d1QCnOtaiY'
    access_token = '803306323467083776-sxV6wMoyG7HPuEmUxQXjKgy8HTEI3LV'
    access_secret = 'POIqPfq7xbcUIbsBG9abHYMIJN2GzXNFPhzigejvt2BGT'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    def save_json(tweet):
        with open('text.json', 'w') as file:
            file.write(json.dumps(tweet))
            tweet = json.loads(json.dumps(tweet))
            return tweet
            print("success")
            # print(json.dumps(tweet))
    for tweet in tweepy.Cursor(api.user_timeline).items(1):
        save_json(tweet._json)

    def process_tweet(tweet):
        with open('text.json', 'r') as file:
            line = file.readline()
            tweet = json.loads(line)
            #print(json.dumps(tweet))
            print("processed")

    process_tweet(tweet)

    def tokens(distros_dict):
        tw = distros_dict['text']
        print(tw)
        print("success")

    with open('text.json', 'r') as f:
        distros_dict = json.load(f)
        # print(distros_dict)
    tokens(distros_dict)


process_or_store()
