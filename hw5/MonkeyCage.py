from BeautifulSoup import BeautifulSoup #or from bs4
import csv 
from nltk.util import clean_html
import urllib2 

page_to_scrape = "http://www.washingtonpost.com/blog/monkey-cage/Archive/201408"

# What info do we want? 
headers = ["IsPost", "Date", "Author", "URL", "Title", "Comments"]

# Where do we save info?
filename = "monkeycage.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

Articles = soup.findAll("div", attrs={'class':'hnews hentry item'})

for article in Articles:
	observation = []
	for item in article.findAll("span", {"id": True}): #Determine if post
		if item["id"] == "mainentry":
			observation.append(1)
		else:
			observation.append(0)
	observation.append(clean_html(str(article.find("span", attrs={"class": "timestamp"})))) #Post date
	observation.append(clean_html(str(article.find("span", attrs={"class": "author vcard"})))) #Authors
	
	past_urls = []
	for item in article.fetch("a"): #URL
		temp_url = item["href"]
		if temp_url[-10:] == "/#comments":
			continue
		elif temp_url[0:7] != "http://":
			continue
		elif str(temp_url) in past_urls:
			continue
		else:
			observation.append(str(temp_url))
			past_urls.append(str(temp_url))
			
	observation.append(clean_html(str(article.find("h2")))) #Post title
	observation.append(clean_html(str(article.find("span", attrs={"class": "count-bubble"})))) #Number of comments
	csvwriter.writerow(observation)
	
readFile.close()