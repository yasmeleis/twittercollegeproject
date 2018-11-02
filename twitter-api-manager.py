# PULLING TWITTER API DATA, DEFINING SEARCH QUERIES, AND ORGANIZING THE OUTPUT FILE:  

# Importing necessary extensions: 
import json
import sys
import time
import twitter
import urllib
import urllib, json, pprint

# Accesseing data through Twitter's API and our developer account:  
from TwitterAPI import TwitterAPI
api = TwitterAPI(
  consumer_key='NWvclDdT8J4XGEGb4X4mv4f7z',
  consumer_secret='B44Orf7O9pbfGQxCmedKswVeqWXfj6odWD5QyuF4xHsvjrcpQa',
  access_token_key='726454687281598467-z2xi3QTl47b86vKmX9hCmJiPRJ1VrON',
  access_token_secret='WWagXKISlQQkNuhr6ARaBGp7owaaTHuqhKBE7dIubrHRJ'
)

# Defining specific search queries for our get request: 
search = api.request('search/tweets', {
	# Search terms using last names of candidates (OR is a query operator):
	'q':'Trump OR Clinton OR Sanders OR Cruz OR Kasich', 
	# Location (New York: latitude,longitude,radius): 
	'geocode':'40.7128,74.0059,500km', 
	# Number of tweets: 
	'count':500, 
	# Only pulling last 500 tweets: 
	'result_type':'recent'
	})

# All the results of the get request will save to an output file 

# Output file name: 
file_name = 'time:' + str(time.time()) + '.txt'

# To open output file: 
f = open(file_name, 'w')

# Transfering code into more readable format: 
output = str(search.json())
output_json = search.json()
statuses = output_json['statuses']

# Tweet count starting with 1: 
tweet_count = 1

# Organizing tweets in output file into more readable format: 
for t in statuses:
	# Tweet number: 
	f.write('Tweet # ' + str(tweet_count) + ':' + '\n')
	tweet_count += 1
	# Time that tweet was created: 
	f.write('created_at: ' + t['created_at'])
	f.write('\n')
	# Content of tweet: 
	f.write('text: ' + t['text'])
	# /n create new lines: 
	f.write('\n')
	f.write('\n')

print("Finished searching the Twitter API. Wrote the results to a file called " + file_name)
