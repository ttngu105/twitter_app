import tweepy

import csv

import pandas as pd

####input your credentials here

consumer_key = 'NV5zWEnXIISXObq0uUuWEYQab'

consumer_secret = 'lJmkNoLYCZxtqxBqrgFSVMOJxJh95XcL43FW4iU5DeZFvxTnId'

access_token = '1221908471429255170-vslxgRHUrwqkN8wi1A5afA4f5A8vzJ'

access_token_secret = 'Mz9EDGcI3QdYKLJ2enJBWIyXH9me6ERFGfUCD8PXxY3cE'

hashtags = ["#Quicken"]



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

#####United Airlines

# Open/Create a file to append data

csvFile = open('ua.csv', 'a')

#Use csv Writer

csvWriter = csv.writer(csvFile)


for i in range(len(hashtags)):
	for tweet in tweepy.Cursor(api.search,q=hashtags[i],count=100,lang="en",since="2017-04-03").items():

	    print (tweet.created_at, tweet.text)

	    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
