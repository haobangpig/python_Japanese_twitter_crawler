#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tweepy import Stream 
 #The Twitter streaming API is used to download twitter messages in real time
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
import tweepy
import time
ckey= 'xxx'
csecret= 'xx'
atoken= 'xx-xx'
asecret= 'xx'

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
