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

base_url = "http://www.azlyrics.com"
# artist_url = "http://www.azlyrics.com/c/coldplay.html"

def get_lyrics_links(artist_url):

	html = urlopen(artist_url) 
	soup = BeautifulSoup(html, "lxml")
	location = soup.find(div, album)
	lyrics_links = [a["href"] for div in location.findAll("div")]
	return lyrics_links

# # make list of URLs
# url_list = []

# # traverse through list of URLs
# def traverse_links(url_list):
# 	for link in url_list:
# 		html = urlopen("link")

# # locate specific elements on page with each URL

# # collect text in elements and write into one single text file
