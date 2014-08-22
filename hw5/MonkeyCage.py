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

#petitions = soup.findAll("a", href=re.compile('^/petition'))
Articles = soup.findAll("div", attrs={'class':'hnews hentry item'})
titles = []
for title in Articles:
  titles.append(clean_html(str(title.find("h2"))))

date = []
for date in Articles:
	date.append(clean_html(str(title.find("timestamp"))))

print Articles
#print titles
#print date

# signatures = soup.findAll("div", attrs={'class':'num-sig'})
# print len(signatures)
# for signature in signatures:
  # s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  # print s

# for i in range(20):
  # petition = petitions[i]
  # p = clean_html(str(petition.find("a")))
  # signature = signatures[i]
  # s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  # csvwriter.writerow([p, s])

readFile.close()