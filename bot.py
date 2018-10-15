# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
CONSUMER_KEY = '1'
CONSUMER_SECRET = '2'
ACCESS_KEY = '3'
ACCESS_SECRET = '4'
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename = open(argfile,'r')
f = filename.readlines()
filename.close()
 
for line in f:
    print("[+] Tuiteando...")
    api.update_status(status = line)
    print("[+] Tuit: ", line)
    time.sleep(900)