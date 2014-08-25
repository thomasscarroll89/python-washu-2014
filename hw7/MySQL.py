#pip install sqlalchemy, pip install pysqlite
import sqlalchemy
import csv 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#START by creating a database for data scraped from monkeycage.com
#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Thomas/hw7A.db', echo=True)
Base = declarative_base() 

readFile = open("C:/Users/Thomas/Documents/GitHub/python-washu-2014/hw5/monkeycage.csv")

class Article(Base):
	__tablename__ = "Articles"
	id = Column(Integer, primary_key=True)
	title = Column(String)
	post = Column(Integer)
	url = Column(String)
	comments = Column(Integer)
	
class Authors(Base):
	__tablename__ = "Authors"
	id = Column(Integer, primary_key=True)
	name = Column(String)

class Date(Base):
	__tablename__ = "Date"
	date = Column(String, primary_key=True) #This does not need a unique identifier since each date must be unique

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

#SECOND create a database for data taken from Twitter
#START by creating a database for data scraped from monkeycage.com
#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Thomas/hw7A.db', echo=True)
Base = declarative_base() 

readFile = open("C:/Users/Thomas/Documents/GitHub/python-washu-2014/hw6/twitter-activity.csv")
dataframe = csv.writer(readFile)
print dataframe["UserName"]

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()