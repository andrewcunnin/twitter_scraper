import tweepy
# Consumer keys and access tokens, used for OAuth
consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_token_secret = 'token secret'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

user = api.me()
