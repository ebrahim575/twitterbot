import tweepy
import twitter_credentials
from contextlib import suppress

ACCESS_TOKEN = '1089954510062145536-6oMv54sW8kOb8RpyLjCVnioVLWVVx2'
ACCESS_TOKEN_SECRET = '0cCeeN6sS8zQ4ejNktQ9fk7PE0EFWP377Yf3dXxOCO6jz'
CONSUMER_KEY = 'b18jz15ozAFauOC5mRIe8ro29'
CONSUMER_SECRET = 'wskbv5skAUzYp5JTNSCWCu3zRrBz3JOKnVYmSKwO1C18JVawTj'

substring = 'PS5'
solelinks = '2698270332'
hammad = '954167026469269504'
ebrahim = '566750505'
ilija = '1290449636281536512'


whitelist = ['RT @', 'LET ME SEE', 'LIKE', 'MILITARY', 'MEDIA','PULSE']

# @solelinks => 2698270332
# @saidlayl = > 1089954510062145536
# @ebz_575 => 566750505

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    with suppress(Exception):
        def on_status(self, status):
            capitalized_tweet = status.text.upper()
            normalTweet = status.text
            userid = str(status.user.id)

            if not any(word in capitalized_tweet for word in whitelist):
                if substring in capitalized_tweet and userid == solelinks:  # ps5 here
                    print('\n\nTweet Found!')
                    print(status.text)
                    api.update_status(normalTweet)
                    print('Tweeting ', normalTweet)
                    print('\nListening again...')
                    return True
            elif userid == solelinks:
                print('\nSoleLinks tweeted : ',normalTweet)

print('PS5 Bot.')
print('\nListening...')
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[solelinks])









