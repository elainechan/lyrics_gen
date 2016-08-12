'''
coldplay_scrape.py
A Web scraper that collects a corpus of Coldplay lyrics.

Functions used:
BeautifulSoup.findAll(tag, attributes, recursive, text, limit, keywords)
BeautifulSoup.find(tag, attributes, recursive, text, keywords)
'''

from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re

# scrape website for URLs
html = urlopen("http://www.azlyrics.com/c/coldplay.html") 
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a",
	href=re.compile("^(/lyrics/coldplay/)((?!:).)*$")): # specify types of links scraped
	if 'href' in link.attrs: 
		print(link.attrs['href'])
		url_list = list(link.attrs['href'])

# # make list of URLs
# url_list = []

# # traverse through list of URLs
# def traverse_links(url_list):
# 	for link in url_list:
# 		html = urlopen("link")

# # locate specific elements on page with each URL

# # collect text in elements and write into one single text file
