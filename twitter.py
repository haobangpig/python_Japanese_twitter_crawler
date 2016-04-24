# encoding: utf-8
import tweepy
import MySQLdb
import json
import re
import time 
consumer_key = "xx"
consumer_secret = "xx"
access_key = "xx-xx"
access_secret = "xx"
users = 'root' # your username
passwd = 'haobang' # your password
host = 'localhost' # your host
db = 'test' # database where your table is stored
table = 'twitter' # table you want to save
table2 = 'user'
con = MySQLdb.connect(user=users, passwd=passwd, host=host, db=db,use_unicode=0,charset='utf8')
c = con.cursor()
con.set_character_set('utf8')
c.execute('SET NAMES utf8mb4;')
c.execute('SET CHARACTER SET utf8mb4;')
c.execute('SET character_set_connection=utf8mb4;')
def get_all_tweets(screen_name):
	#initialize a list to hold all the tweepy Tweets
	alltweets = []		
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)	
	#save most recent tweets
	alltweets.extend(new_tweets)
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)		
		#save most recent tweets
		alltweets.extend(new_tweets)		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1		
		print "...%s tweets downloaded so far" % (len(alltweets))
	return alltweets


if __name__ == '__main__':
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	#pass in the username of the account you wa	nt to download
	
	query = "SELECT screen_name FROM %s;" % table2
	c.execute(query)
	result=c.fetchall()
	count =0
	#for users in result:
	for users in result:
		try:
			user=users[0]
			all = get_all_tweets(user)
			for tweet in all:
				time = [tweet.created_at]
				id = [tweet.id_str]
				language= [tweet.lang]
				text = [tweet.text.encode("utf-8")]
				c.execute("INSERT INTO twitter (time,language,id,text) VALUES (%s,%s,%s,%s)",(time,language,id,text))
		except Exception, e:
			print e
			c.execute("delete from user where screen_name=%s", users)
			continue
		c.execute("delete from user where screen_name=%s", users)
		con.commit()
