import requests
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


screen_name = raw_input("\nPlease enter the Twitter handle experiencing harassment, including @: ")

start_date = raw_input("What date do you want to start from? (mm/dd/yyyy): ")
end_date = raw_input("What date do you want to end on? (mm/dd/yyyy): ")

alltweets = []

print "\n\nOk, you want to capture mentions of {} from {} to {}.\n\n...\n\nGrabbing tweets now...\n".format(screen_name, start_date, end_date)

'''
try:
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q = screen_name, count=1)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
            

    print alltweets
    print "...%s tweets downloaded" % (len(alltweets))
    
except tweepy.TweepError, e:
    print e
'''