# encoding: utf-8
import tweepy
import MySQLdb
import json
import re
consumer_key = "Y3QHmimWrVJKySnjnAA1eWZTf"
consumer_secret = "m8MRiZFUSi50M4dYVJIzWvnUGeLSfn6FqgEKSr4bipCa6NvlXN"
access_key = "717953299958247424-Au3CpITFDW7CpYzIZghzhfc34pQuGvz"
access_secret = "H32sWHVzy3J5ehbrycg22rfu805yabqYXgF7el7HQX6aP"
users = 'root' # your username
passwd = 'haobang' # your password
host = 'localhost' # your host
db = 'test' # database where your table is stored
table = 'twitter' # table you want to save
table2 = 'user'

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
	#pass in the username of the account you want to download
	con = MySQLdb.connect(user=users, passwd=passwd, host=host, db=db,use_unicode=0,charset='utf8')
	cursor = con.cursor()
	query = "SELECT screen_name FROM %s;" % table2
	cursor.execute(query)
	result=cursor.fetchall()
	count =0;
	#for users in result:
	for users in result:
		alltweets=get_all_tweets("haobangpig")
		cursor = con.cursor()
		string = ''.join(alltweets)
		print string
		'''
	        if 'Status' in tweet:
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
	            con.execute("INSERT INTO twitter_ja (time, id, language,screen_name,username,location,text) VALUES (%s,%s,%s,%s,%s,%s,%s)",(time,ids,language,screen_name,username,location,text))






		for tweet in alltweets:
			cursor.execute("INSERT INTO twitter (time,id,language,screen_name,location) VALUES (alltweets['created_at'],alltweets['id_str'],alltweets['lang'],user['screen_name'],user['location'],%s"),(alltweets['text'].encode('utf-8'))
		cursor.close()
		con.commit()
		'''
