import tweepy
import time

consumer_key =
consumer_secret =
key =
secret =

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = ""
tweetNumber = 1

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

for tweet in tweets:
    try:
        tweet.retweet()
        print("Retweet Done!")
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(2)



