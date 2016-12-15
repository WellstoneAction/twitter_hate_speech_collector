import requests
import pprint
import datetime
import csv
from datetime import timedelta
import tweepy
from keys import *

#Twitter API credentials
#consumer_key = ""
#consumer_secret = ""
#access_key = ""
#access_secret = ""

# Credentialing
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

help = "Dumps tweets to csv (with digital fingerprint) for user accounts experiencing harassment"


screenname = raw_input("\nPlease enter the Twitter handle experiencing harassment, including '@': ").strip()
since_tweet = raw_input("What tweet do you want to start from?: ")
maxTweets = 1000000
total = 0
max_id = -1L
print max_id

print "\n\nOk, you want to capture mentions of {} starting from tweet number {}.\n\n...\n\nGrabbing tweets now...\n".format(screenname, since_tweet)

with open('twitter_results.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter = ",", quotechar = '"')
    writer.writerow(["Tweet ID", "Direct response to Wintana's original status?", "Sent when?", "Sender", "Sender's name", "Text" , "In reply to what tweet, if any?",  "Data source"])
    while total < maxTweets:
        try:
            if(max_id <=0):
                new_tweets = api.search(q = screenname+ " -filter:retweets", since_id = since_tweet, count =100)
            else:
                new_tweets = api.search(q = screenname+ " -filter:retweets", since_id = since_tweet, max_id = str(max_id-1), count = 100)
            if not new_tweets:
                print("That's it!")
                break
            for t in new_tweets:
                ttext = t.text.encode('UTF-8')
                tauthorhandle = t.user.screen_name.encode('UTF-8')
                tauthor = t.author.name.encode('UTF-8')
                if t.in_reply_to_status_id == since_tweet:
                    flag = "Yes"
                else:
                    flag = ""
                writer.writerow([t.id, flag, t.created_at, tauthorhandle, tauthor, ttext, t.in_reply_to_status_id, t._api])
            max_id = new_tweets[-1].id
            print max_id
            total += len(new_tweets)
            print total
        except tweepy.TweepError as e:
            print e


# the bad thread is: in_reply_to_status_id=803681534746169344