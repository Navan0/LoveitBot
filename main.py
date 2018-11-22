import tweepy
import json
from tweepy import OAuthHandler

consumer_key = '4IjEmWFE289MmeIqjcY5WBqow'
consumer_secret = 'PXNBzRcPNdEIygVl6C5eBH8r6hKPpLDmzff3Hil4d1QCnOtaiY'
access_token = '803306323467083776-sxV6wMoyG7HPuEmUxQXjKgy8HTEI3LV'
access_secret = 'POIqPfq7xbcUIbsBG9abHYMIJN2GzXNFPhzigejvt2BGT'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_or_store(tweet):
    file = open("text.json", "w")
    file.write(json.dumps(tweet))


for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
