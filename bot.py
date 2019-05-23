#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:59:35 2019

@author: markditsworth
"""
import tweepy
import secret
import requests
#import time
#import multiprocessing

print("performing OAuth...")
auth = tweepy.OAuthHandler(secret.api_key, secret.api_secret_key)
auth.set_access_token(secret.access_token, secret.access_token_secret)
api = tweepy.API(auth)

def download(page_link):
    if '/abs/' in page_link:
	end = page_link.split('/')[-1]
	link = 'https://arxiv.org/pdf/'+end+'.pdf'
	paper_name = ''.join(end.split('.'))+'.pdf'
	r = requests.get(link)
	print("downloading link from %s..."%link)
	with open(paper_name, 'wb') as fObj:
	    fObj.write(r.content)
	print("done")
    elif '.pdf' == page_link[-4:]:
	r = requests.get(page_link)
	paper_name = page_link.split('/')[-1]
	print("downloading link from %s..."%page_link)
	with open(paper_name, 'wb') as fObj:
	    fObj.write(r.content)
	print("done")
	

class BotStreamer(tweepy.StreamListener):
    def on_status(self,status):
	username = status.user.screen_name
	if username == secret.username:
	    status_id_in_reply_to = status.in_reply_to_status_id
	    parent_status = api.statuses_lookup([status_id_in_reply_to])[0]
	    link = parent_status.entities['urls'][0]['expanded_url']
	    download(link)
    def on_error(self, status_code):
	print("Error: " + repr(status_code))
 
    def on_timeout(self):
	print("Timeout...")
    
    def on_disconnect(self, notice):
	print("Disconnect.")
	print(notice)

def main():
    print("Authenticated!")
    # start app
    myListener = BotStreamer()
    stream = tweepy.Stream(auth,myListener)
    try:
        stream.filter(track=[secret.bot_handle])
    except Exception as ex:
        print('exception: {}'.format(ex))
        print('Reconnecting...')
        main()
	
if __name__ == '__main__':
main()
