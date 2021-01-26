import tweepy
import twitter_credentials
from contextlib import suppress
from twilio.rest import Client

#twitter
ACCESS_TOKEN = '1089954510062145536-6oMv54sW8kOb8RpyLjCVnioVLWVVx2'
ACCESS_TOKEN_SECRET = '0cCeeN6sS8zQ4ejNktQ9fk7PE0EFWP377Yf3dXxOCO6jz'
CONSUMER_KEY = 'b18jz15ozAFauOC5mRIe8ro29'
CONSUMER_SECRET = 'wskbv5skAUzYp5JTNSCWCu3zRrBz3JOKnVYmSKwO1C18JVawTj'

#twilio
account_sid = 'AC6725186a0213068ed6c26c31c61ff7dc'
auth_token = 'bcf7bf3e9b3a433db5e4c2406dd17052'

substring = 'NEW MUSIC OUT NOW'
raphubdaily = '3114427119'
ilija = '1290449636281536512'


whitelist = []

# @solelinks => 2698270332
# @saidlayl = > 1089954510062145536
# @ebz_575 => 566750505
# @raphubdaily => 3114427119



contacts = {
    'my_cell': '+16303634339',
    'umar_cell' : '+16307858333',
    'mum_cell' : '+16307969690',
    'dhiral_cell' : '+447952711349',
    'suf_twilio' : '+16503983501',
    'my_twilioUS' : '+13122623895',
    'my_twilioGB' : '+447723144969',
}

#twitter
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#twilio
client = Client(account_sid, auth_token)
while 1:
    try:
        def text(msg):
            message = client.messages.create(
                body=msg,
                from_=contacts['my_twilioUS'],
                to=contacts['my_cell']
            )
            message = client.messages.create(
                body=msg,
                from_=contacts['my_twilioGB'],
                to=contacts['dhiral_cell']
            )
            print(msg, '\t', message.sid)


        class MyStreamListener(tweepy.StreamListener):
            with suppress(Exception):
                def on_status(self, status):
                    capitalized_tweet = status.text.upper()
                    normalTweet = status.text
                    userid = str(status.user.id)
                    if substring in capitalized_tweet and userid == raphubdaily and capitalized_tweet not in whitelist: #ps5 here
                        print('\n\nTweet Found!')
                        print(status.text)
                        text(normalTweet)
                        print('\nListening again...')
                        return True
                    elif userid == raphubdaily:
                        print('\nRapHubDaily tweeted : ',normalTweet)
        print('RapHubDaily.')
        print('\nListening...')
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(follow=[raphubdaily])
    except:
        pass










