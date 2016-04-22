#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tweepy import Stream 
 #The Twitter streaming API is used to download twitter messages in real time
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
import tweepy
import time
ckey= 'Y3QHmimWrVJKySnjnAA1eWZTf'
csecret= 'm8MRiZFUSi50M4dYVJIzWvnUGeLSfn6FqgEKSr4bipCa6NvlXN'
atoken= '717953299958247424-Au3CpITFDW7CpYzIZghzhfc34pQuGvz'
asecret= 'H32sWHVzy3J5ehbrycg22rfu805yabqYXgF7el7HQX6aP'

#Therefore using the streaming api has three steps.
#Create a class inheriting from StreamListener
#Using that class create a Stream object
#Connect to the Twitter API using the Stream.

auth=OAuthHandler(ckey, csecret) 
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
user = api.get_user('kanamin6290')
print "My Twitter Handle:", user.screen_name
ct = 0
print user.friends_count
for friend in tweepy.Cursor(api.friends, screen_name=user.screen_name,count = 200).items():
	   print friend.screen_name
	   ct=ct+1;

print "\n\nFinal Count:", ct