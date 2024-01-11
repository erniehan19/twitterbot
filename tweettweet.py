import tweepy
import time

auth = tweepy.OAuthHandler("08sPSORpedtfuvrTtb52IPtcD", "MSvmdW6ycSqDBMQGiAXozCE3u5FRn2SeXRmbHWEzgDNyHttQ9M")
auth.set_access_token("1745254390934708224-JKrzQdOGL84mtg4TxE6b0J0MwnCF9T", "4i2GCxyKd0RbsQ9cOJ8uxgRnlfbNpNYMYo9ywCKGTi1l7")

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#follows back users with more than 100 followers
def twitter_follow_back ():
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.followers._count > 100:
            follower.follow()

#searches for specific word and the number of tweets you want to like and likes it for you
def twitter_like(search_string, numbersOfTweets):
    for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
        try:
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
