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

start_date = raw_input("What date do you want to start from? (yyyy-mm-dd): ").strip()
end_date = raw_input("What date do you want to end on? (yyyy-mm-dd): ").strip()

alltweets = []

print "\n\nOk, you want to capture mentions of {} from {} to {}.\n\n...\n\nGrabbing tweets now...\n".format(screenname, start_date, end_date)

with open('twitter_results.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter = ",", quotechar = '"')
    writer.writerow(["Tweet ID", "Part of the original thread?", "Sent when", "Sent by whom", "Data source", "In reply to what tweet", "text"])
    try:
        new_tweets = api.search(q = screenname, since="2016-11-29")
        print len(new_tweets)
        for t in new_tweets:
            ttext = t.text.encode('UTF-8')
            tauthor = t.author.name.encode('UTF-8')
            if tweet.in_reply_to_status_id == 809166899334488064:
                flag = "Yes"
            else:
                flag = ""
            writer.writerow([t.id, flag, t.created_at, tauthor, t._api, t.in_reply_to_status_id, ttext])
        print t
    except tweepy.TweepError as e:
        print e


# the bad thread is: in_reply_to_status_id=809166899334488064