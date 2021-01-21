import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

substring = 'PS5'

class StdOutListener(StreamListener):
    def on_status(self,status):
        print(status.text)
        print(type(status))

        return True

    def on_error(self,status):
        print('Error # ',status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    api = tweepy.API(auth)
    #api.update_status('Wow great Success!')

    # This line filter Twitter Streams to capture data by the keywords:
    #stream.filter(follow= ['1089954510062145536'],track=['hello world'])
    stream.filter(follow= ['1089954510062145536'])

    #stream.filter(track=['trump'])

    #@solelinks => 2698270332
    #@saidlayl = > 1089954510062145536
