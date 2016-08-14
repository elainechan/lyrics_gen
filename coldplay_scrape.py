'''
coldplay_scrape.py
A Web scraper that collects a corpus of Coldplay lyrics.

Functions used:
BeautifulSoup.findAll(tag, attributes, recursive, text, limit, keywords)
BeautifulSoup.find(tag, attributes, recursive, text, keywords)
'''

import urllib.request
from bs4 import BeautifulSoup

def get_lyrics_links(artist_url, local_filename):
	local_filename, headers = urllib.request.urlretrieve('http://www.azlyrics.com/c/coldplay.html')
	html = open(local_filename)
	soup = BeautifulSoup(html, 'html.parser')
	return soup.prettify()
	print(soup.prettify())
	# locations = soup.findAll(id='listAlbum')
	# return locations
	# print(len(locations))

get_lyrics_links('http://www.azlyrics.com/c/coldplay.html', 'url_resource.html')

# # make list of URLs
# url_list = []

# # traverse through list of URLs
# def traverse_links(url_list):
# 	for link in url_list:
# 		html = urlopen("link")

# # locate specific elements on page with each URL

# # collect text in elements and write into one single text file
