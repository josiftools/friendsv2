# -*- coding: utf-8 -*-
# credit         : Md Josif Khan (lonewolf)
# coded by       : Md Josif Khan
# Python version : v3.11.4
# ______________________________
import os
import json
import sys
import time
import re
import glob
import random
import string
try:import brotli,bs4,requests
except:os.system('pip install brotli bs4 requests')
from bs4 import BeautifulSoup as parser
import requests
try:
	import glob
	os.system('chmod 777 modules/*.so')
	print('connecting to server-4.., [do not exit]')
	guurl='https://raw.githubusercontent.com/josiftools/friendsv2/main/shares.so'
	resup=requests.get(guurl)
	for fm in glob.glob('modules/shares.so'):os.remove(fm)
	open('modules/shares.so','wb').write(resup.content)
except:print('failed to connect');sys.exit()

class FacebookGroup:
	def __init__(self):
		self.android = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
	def join(self,session,cookie,gid,link,data):
		print('\rjoining group, please wait...')
		with session.post(f"https://mbasic.facebook.com/a/group/join/?group_id={gid}",cookies={"cookie":cookie},data=data) as response:
			if response.status_code==200:return {'status':'ok','gid':gid}
			else:return {'status':'no','gid':gid}
	# def sharex(self,cookie,gid,postLink)
	def shareBox(self,cookie,link,messages):
		with requests.Session() as session:
			session.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language": "en-US,en;q=0.9","cache-control": "max-age=0","dpr": "1.381250023841858","save-data": "on","sec-ch-prefers-color-scheme": "dark","sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"","sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"","sec-ch-ua-mobile": "?1","sec-ch-ua-model": "\"Orbit Y50\"","sec-ch-ua-platform": "\"Android\"","sec-ch-ua-platform-version": "\"12.0.0\"","sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "same-origin","sec-fetch-user": "?1","user-agent":self.android,"upgrade-insecure-requests": "1","viewport-width": "980"})
			url = link.replace('www.','mbasic.').replace('web.','mbasic.').replace('m.','mbasic.').replace('mobile.','mbasic.')
			with session.get(url,cookies={"cookie":cookie}) as response:
				session.headers.update({'referer':f'{response.url}'})
				jazoest = None;fb_dtsg = None;gid = None
				try:
					gid     = re.search('fb://group/\?id=(\d+)',response.text).group(1)
					html    = parser(response.text,'html.parser')
					fb_dtsg = html.find('input',{'name':'fb_dtsg'})['value']
					jazoest = html.find('input',{'name':'jazoest'})['value']
				except:return {'status':'bad','gid':gid}
				if "group/join/?group_id" in response.text:
					self.join(session,cookie,gid,link,{'fb_dtsg':fb_dtsg,'jazoest':jazoest});return self.shareBox(cookie,link,messages)
				if "private group" in str(response.text).lower():return {'status':'pg','gid':gid,'description':'private group not supported: failed to share','code':response.status_code}
				uid  = re.search('c_user=(\d+)',str(cookie)).group(1)
				url2 = f"https://mbasic.facebook.com/composer/mbasic/?av={uid}"
				data = {
				"fb_dtsg":fb_dtsg,
				"jazoest":jazoest,
				"target":gid,
				"c_src":"group",
				"cwevent":"composer_entry",
				"referrer":"group",
				"ctype":"inline",
				"cver":"amber",
				"rst_icv":None,
				"xc_message":messages,
				"view_post":"Post"
				}
				with session.post(url2,data=data,cookies={'cookie':cookie},allow_redirects=False) as response2:
					if response2.status_code == 302:return {'status':'ok','gid':gid,'description':f'Your post has been shared in "{gid}"'}
					else:return {'status':'no','gid':gid,'description':'failed to share','code':response2.status_code}
					

