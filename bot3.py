import tweepy
import twitter_credentials
from contextlib import suppress

substring = 'PS5'
walmartSubstr = 'WALMART'
bestbuySubstr = 'BESTBUY'

solelinks = '2698270332'
hammad = '954167026469269504'
ebrahim = '566750505'
IlijaVidic = '1290449636281536512'
passwordSubstr = 'PASSWORD'
rtSubstr = 'RT @'
wSubstr = 'LET ME SEE'
likeSubstr = 'LIKE'
militarySubstr = 'MILITARY'

# @solelinks => 2698270332
# @saidlayl = > 1089954510062145536
# @ebz_575 => 566750505

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

whitelist = ['RT @', 'LET ME SEE', 'LIKE', 'MILITARY', 'MEDIA']

class MyStreamListener(tweepy.StreamListener):
    with suppress(Exception):
        def on_status(self, status):
            capitalized_tweet = status.text.upper()
            normalTweet = status.text
            userid = str(status.user.id)
            if substring in capitalized_tweet and (userid == solelinks and rtSubstr not in normalTweet and wSubstr not in capitalized_tweet and likeSubstr not in capitalized_tweet): #ps5 here
                print('\n\nTweet Found!')
                print(status.text)
                api.update_status(normalTweet)
                print('Tweeting ', normalTweet)
                print('\nListening again...')
                return True
            elif userid == solelinks:
                print('\nSoleLinks tweeted : ',normalTweet)

print('\nListening...')
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[solelinks or IlijaVidic or hammad or ebrahim])









