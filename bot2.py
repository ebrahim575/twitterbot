import tweepy
import twitter_credentials
from contextlib import suppress
import webbrowser

substring = 'PS5'
walmartSubstr = 'WALMART'
bestbuySubstr = 'BESTBUY'

solelinks = '2698270332'
hammad = '954167026469269504'
IliyaVidic = '1290449636281536512'

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    with suppress(Exception):
        def on_status(self, status):
            tweet = status.text.upper()
            tweet2 = status.text
            userid = str(status.user.id)
            if substring in tweet and userid == solelinks: #ps5 here
                print('\n\nTweet Found!')
                print(status.text)
                api.update_status(tweet2)
                webbrowser.open('https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816')
                webbrowser.open('https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817')
                print('Tweeting ', tweet2)
                print('\nListening again...')
                return True
            elif walmartSubstr in tweet and userid == solelinks:
                webbrowser.open('https://affil.walmart.com/cart/addToCart?items=363472942')

            elif bestbuySubstr in tweet and userid == solelinks:
                webbrowser.open('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
                webbrowser.open('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161')
            elif userid == solelinks:
                print('\nSolelinks tweeted : ',tweet2)

print('\nListening...')
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[solelinks])


# @solelinks => 2698270332
# @saidlayl = > 1089954510062145536
# @ebz_575 => 566750505








