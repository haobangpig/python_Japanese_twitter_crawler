# -*- coding: utf-8 -*-
 
import sys
import json
import tweepy 
import re
import MySQLdb
import time
# Account
consumer_key= 'Y3QHmimWrVJKySnjnAA1eWZTf'
consumer_secret= 'm8MRiZFUSi50M4dYVJIzWvnUGeLSfn6FqgEKSr4bipCa6NvlXN'
access_token= '717953299958247424-Au3CpITFDW7CpYzIZghzhfc34pQuGvz'
access_token_secret= 'H32sWHVzy3J5ehbrycg22rfu805yabqYXgF7el7HQX6aP'

conn=MySQLdb.Connection("localhost","root","haobang","test");
c = conn.cursor()
conn.set_character_set('utf8')
c.execute('SET NAMES utf8mb4;')
c.execute('SET CHARACTER SET utf8mb4;')
c.execute('SET character_set_connection=utf8mb4;')
class Listener(tweepy.streaming.StreamListener):
    def on_data(self, data):
        if data.startswith("{"):
            tweet = json.loads(data)
            if 'text' in tweet:
                user = tweet['user']
                time= tweet['created_at']
                ids = tweet['id']
                language=tweet['lang']
                screen_name=user['screen_name'].encode('utf-8')
                username=user['name'].encode('utf-8')
                location=user['location']
                text = re.sub(r'\n',r' ',tweet['text'].encode('utf-8')) # 改行コード除去
                print tweet['created_at'],":\t",tweet['id'],":\t",tweet['lang'],":\t",user['screen_name'].encode('utf-8'),":\t", \
                              user['name'].encode('utf-8'),":\t Location：", user['location'],":",text
            
                c.execute("INSERT INTO twitter_ja (time, id, language,screen_name,username,location,text) VALUES (%s,%s,%s,%s,%s,%s,%s)",(time,ids,language,screen_name,username,location,text))             
                conn.commit()
        return True
 
    def on_error(self, status):
        print status
 



if __name__ == '__main__':
    l = Listener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    stream = tweepy.Stream(auth, l)
#    filterの宣言部分 @ /usr/local/lib/python2.7/dist-packages/tweepy/streaming.py
#    def filter(self, follow=None, track=None, async=False, locations=None,
#        count = None, stall_warnings=False, languages=None):
#    パラメータの使い方は https://dev.twitter.com/docs/streaming-apis/parameters
    # keywords = ['A','B']  
    #filter(track=[keywords])
    stream.filter(languages=['ja'],track=[u'共産党',u'日本',u'地震'])
