#pip install sqlalchemy, pip install pysqlite
import sqlalchemy
import csv 
import pandas 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#START by creating a database for data scraped from monkeycage.com
#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Thomas/hw7monkey.db', echo=True)
Base = declarative_base() 

dataframe = pandas.read_csv("C:/Users/Thomas/Documents/GitHub/python-washu-2014/hw5/monkeycage.csv")
dataframe["Date"] = dataframe["Date"].str[-10:]

class Article(Base):
	__tablename__ = "Article"
	id = Column(Integer, primary_key=True)
	title = Column(String)
	author = Column(String)
	post = Column(Integer)
	url = Column(String)
	comments = Column(Integer)
	date_id = Column(Integer, ForeignKey("Date.id"))
		
	def __init__(self, title, author, post, url, comments, date):
		self.title=title
		self.author = author
		self.post=post
		self.url=url
		self.comments=comments
		self.date = date
	
	def __repr__(self):
		return self.title


class Date(Base):
	__tablename__ = "Date"
	id = Column(Integer, primary_key=True) #id will just be numbers 1-31, indicating the date in August (since we're only looking at the month of August)
	date = Column(String) 
	articles = relationship(Article, backref="date")
	
	def __init__(self, date):
		self.date=date
	
	def __repr__(self):
		return self.date

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()
	
#Store the different dates, formatted as mm/dd/yyyy
for day in range(1, 32):
	if day < 10: #for the first 9 days we add another 0 to the day, so we have the same number of characters for each date
		date = Date(date="08/0" + str(day) + "/2014")
		session.add(date)
	else:
		date = Date(date="08/" + str(day) + "/2014")
		session.add(date)

for row in range(0, len(dataframe.index)):
	temp_date = Date(dataframe["Date"][row])
	temp_title = str(dataframe["Title"][row].decode("utf-8").encode('cp850','replace').decode('cp850')) #This solves part of an encoding issue I was having
	temp_authors = dataframe["Author"][row].decode("utf-8").encode('cp850','replace').decode('cp850') #Still not perfect; it replaces some quotes/apostrophes
	temp_url = str(dataframe["URL"][row].decode("utf-8").encode('cp850','replace').decode('cp850')) #with question marks, but I can't for the life of me get this 
																									#thing to encode/decode correctly and it won't run otherwise
	article = Article(title=temp_title, author=temp_authors, post=int(dataframe["IsPost"][row]), url=temp_url, comments=int(dataframe["Comments"][row]),
		date=temp_date)
	session.add(article)

#session.commit()
	
for article in session.query(Article):
	print article.title, article.date
	
#####################################################
#SECOND create a database for data taken from Twitter
#START by creating a database for data scraped from twitter.com
#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Thomas/hwtwitter.db', echo=True)
Base = declarative_base() 

dataframe = pandas.read_csv("C:/Users/Thomas/Documents/GitHub/python-washu-2014/hw6/twitter-activity.csv")
dataframe["StartDate"] = dataframe["StartDate"].str[0:10] #extracts just the date in format mm-dd-yyyy

#Create Classes
class User(Base):
	__tablename__ = "User"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	Num_Followers = Column(Integer)
	Num_Friends = Column(Integer)
	Num_Tweets = Column(Integer)
	day_id = Column(Integer, ForeignKey("StartDay.id"))
	month_id = Column(Integer, ForeignKey("StartMonth.id"))
	year_id = Column(Integer, ForeignKey("StartYear.id"))

	def __init__(self, name, followers, friends, tweets, month, day, year):
		self.name=name
		self.followers = followers
		self.friends=friends
		self.tweets=tweets
		self.month=month
		self.day=day
		self.year = year
		self.date = str(month) + "/" + str(day) + "/" + str(year)
		
	def __repr__(self):
		return self.name

class StartMonth(Base):
	__tablename__ = "StartMonth"
	id = Column(Integer, primary_key=True)
	month = Column(String)
	users = relationship(User, backref="month")

	def __init__(self, month):
		self.month=month
		
	def __repr__(self):
		return self.month

class StartDay(Base):
	__tablename__ = "StartDay"
	id = Column(Integer, primary_key=True)
	day = Column(String)
	users = relationship(User, backref="day")

	def __init__(self, day):
		self.day=day
		
	def __repr__(self):
		return self.day

class StartYear(Base):
	__tablename__ = "StartYear"
	id = Column(Integer, primary_key=True)
	year = Column(String)
	users = relationship(User, backref="year")

	def __init__(self, year):
		self.year=year
		
	def __repr__(self):
		return self.year

		
#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

#Create 3 tables, one for the years (2000 on), one for the months, and one for the dates
for iyear in range(2000, 2015):
	temp_year = StartYear(year=str(iyear))
	session.add(temp_year)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for imonth in months:
	temp_month = StartMonth(month=imonth)
	session.add(temp_month)

for iday in range(1, 32):
	temp_day = StartDay(day=iday)
	session.add(temp_day)
	
for row in range(0, len(dataframe.index)):
	temp_day = StartDay(dataframe["StartDate"][row][-2:])
	temp_month = StartMonth(dataframe["StartDate"][row][5:7])
	temp_year = StartYear(dataframe["StartDate"][row][0:4])
	temp_name = str(dataframe["UserName"][row].decode("utf-8").encode('cp850','replace').decode('cp850'))
	temp_followers = dataframe["Followers"][row]
	temp_friends = dataframe["Following"][row]
	temp_tweets = dataframe["TotalTweets"][row]
	user = User(name=temp_name, followers=temp_followers, friends=temp_friends, tweets=temp_tweets, month=temp_month, day=temp_day, year=temp_year)
	session.add(user)

#session.commit()
for user in session.query(User).join(StartMonth):
	print "Matt is followed by " + user.name + ", who joined on " + user.month.month + "/" + user.day.day + "/" + user.year.year 

#####################################################
#THIRD create a database for the second dataset that was scraped from Twitter
#START by creating a database for data scraped from twitter.com
#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Thomas/hwtwitter2.db', echo=True)
Base = declarative_base() 

dataframe = pandas.read_csv("C:/Users/Thomas/Documents/GitHub/python-washu-2014/hw6/twitter-activity2.csv")
dataframe["StartDate"] = dataframe["StartDate"].str[0:10] #extracts just the date in format mm-dd-yyyy

#Create Classes
class User(Base):
	__tablename__ = "User"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	Num_Followers = Column(Integer)
	Num_Friends = Column(Integer)
	Num_Tweets = Column(Integer)
	day_id = Column(Integer, ForeignKey("StartDay.id"))
	month_id = Column(Integer, ForeignKey("StartMonth.id"))
	year_id = Column(Integer, ForeignKey("StartYear.id"))

	def __init__(self, name, followers, friends, tweets, month, day, year):
		self.name=name
		self.followers = followers
		self.friends=friends
		self.tweets=tweets
		self.month=month
		self.day=day
		self.year = year
		self.date = str(month) + "/" + str(day) + "/" + str(year)
		
	def __repr__(self):
		return self.name

class StartMonth(Base):
	__tablename__ = "StartMonth"
	id = Column(Integer, primary_key=True)
	month = Column(String)
	users = relationship(User, backref="month")

	def __init__(self, month):
		self.month=month
		
	def __repr__(self):
		return self.month

class StartDay(Base):
	__tablename__ = "StartDay"
	id = Column(Integer, primary_key=True)
	day = Column(String)
	users = relationship(User, backref="day")

	def __init__(self, day):
		self.day=day
		
	def __repr__(self):
		return self.day

class StartYear(Base):
	__tablename__ = "StartYear"
	id = Column(Integer, primary_key=True)
	year = Column(String)
	users = relationship(User, backref="year")

	def __init__(self, year):
		self.year=year
		
	def __repr__(self):
		return self.year

		
#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

#Create 3 tables, one for the years (2000 on), one for the months, and one for the dates
for iyear in range(2000, 2015):
	temp_year = StartYear(year=str(iyear))
	session.add(temp_year)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for imonth in months:
	temp_month = StartMonth(month=imonth)
	session.add(temp_month)

for iday in range(1, 32):
	temp_day = StartDay(day=iday)
	session.add(temp_day)
	
for row in range(0, len(dataframe.index)):
	temp_day = StartDay(dataframe["StartDate"][row][-2:])
	temp_month = StartMonth(dataframe["StartDate"][row][5:7])
	temp_year = StartYear(dataframe["StartDate"][row][0:4])
	temp_name = str(dataframe["UserName"][row].decode("utf-8").encode('cp850','replace').decode('cp850'))
	temp_followers = dataframe["Followers"][row]
	temp_friends = dataframe["Following"][row]
	temp_tweets = dataframe["TotalTweets"][row]
	user = User(name=temp_name, followers=temp_followers, friends=temp_friends, tweets=temp_tweets, month=temp_month, day=temp_day, year=temp_year)
	session.add(user)

#session.commit()
for user in session.query(User).join(StartMonth):
	print "Matt follows " + user.name + ", who joined on " + user.month.month + "/" + user.day.day + "/" + user.year.year 	