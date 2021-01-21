import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
option = int(input('Press 1 if you would like to delete all tweets : '))
counter = 1
if option == 1:
    print("Retrieving tweets")
    timeline = tweepy.Cursor(api.user_timeline).items()
    print('Deleting Tweets...')

    for tweet in timeline:

        print('Deleting tweet #',counter)
        counter = counter  + 1
        api.destroy_status(tweet.id)
    print('Deleted all tweets')

else:
    print('Not Deleting Tweets or entered wrong option.')