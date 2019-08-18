#!/usr/bin/python

from mechanize import Browser
from bs4 import BeautifulSoup
import json, sys, re

b = Browser()
b.set_handle_robots(False)
b.set_handle_refresh(False)
b.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Windows Phone 6.5.3.5)')] # Facebook still supports Windows Phone 6.5, the greatest mobile OS ever written. Long may it continue.

data = sys.argv[1:]
events = []
ret = []

for pageid in data:

	url = "https://m.facebook.com/" + pageid + "?v=events"

	r = b.open(url)
	html = r.read()

	for a in b.links():

		if not(a.absolute_url.startswith('https://m.facebook.com/events/')):
			continue

		events.append(re.sub(r"[^0-9].*$", '', a.absolute_url.replace('https://m.facebook.com/events/', '')))

for fbid in events:

	url = 'https://m.facebook.com/' + fbid

	r = b.open(url)
	html = r.read()

	soup = BeautifulSoup(html, 'lxml')

	for tag in soup.find_all("script", type="application/ld+json"):
		data = json.loads(tag.text)
		data['id'] = fbid
		ret.append(data)

print json.dumps(ret)
