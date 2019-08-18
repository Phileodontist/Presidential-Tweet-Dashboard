import twitter
import tweepy
import csv
import json
from tweepy import API 
from tweepy import TweepError
from tweepy import OAuthHandler 
from time import sleep

with open('api_keys.json') as tf:
	keys = json.load(tf)

# Specify User
user = 'realDonaldTrump' 

'''
def authenticate():
	auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
	auth.set_access_token(keys['access_token'], keys['access_token_secret'])

	return tweepy.API(auth)
'''

def authenticate():
	return twitter.Api(keys['consumer_key'], keys['consumer_secret'],keys['access_token'], keys['access_token_secret'])

if __name__ == "__main__":
	api = authenticate()
	'''
	public_tweets = api.user_timeline()
	for tweet in public_tweets:
		with open('test.txt', 'a') as tf:
			tf.write(tweet.text.encode('utf-8'))
			print(tweet.text)

	#output_file = '{}.json'.format(user)
	'''
	statuses = api.GetUserTimeline(screen_name=user, count=199)
	for status in statuses:
		with open('test.txt', 'a') as tf:
			tf.write(status.text.encode('utf-8') + '\n')
			print(status.text)
	

