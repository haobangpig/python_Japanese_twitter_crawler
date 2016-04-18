# -*- coding: utf-8 -*-
import MySQLdb
import csv

user = 'root' # your username
passwd = 'haobang' # your password
host = 'localhost' # your host
db = 'test' # database where your table is stored
table = 'twitter_en' # table you want to save

con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
cursor = con.cursor()

query = "SELECT text FROM %s;" % table
cursor.execute(query)
c=csv.writer(open("data.csv","wb"))
result=cursor.fetchall()
for row in result:
    c.writerow(row)