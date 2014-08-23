import tweepy
import time
import csv 
import pandas 
import sys
from datetime import date, datetime

FollowersData = pandas.read_csv("twitter-activity.csv")
FollowingData = pandas.read_csv("twitter-activity2.csv")

#Answer to question 1
user_name = FollowersData["UserName"][FollowersData["Followers"] == max(FollowersData["Followers"])]
print "Follower with most followers is " + (str(user_name.values)[2:-2]) + " with " + str(max(FollowersData["Followers"])) + " followers."

#Answer to question 4
#Add a new column representing the level of activity, which is defined as the average number of tweets per day. 

current_day = datetime.strptime("2014-08-23", "%Y-%m-%d")
begin_date = []
days_active = []
for row_number in range(0, len(FollowingData["StartDate"].values)):
	begin_date.append(FollowingData["StartDate"].values[row_number][:10])
	begin_date[row_number] = datetime.strptime(begin_date[row_number], "%Y-%m-%d")
	total_time = current_day - begin_date[row_number]
	days_active.append(total_time.days)

FollowingData["Activity"] = FollowingData["TotalTweets"]/days_active
most_active = FollowingData["UserName"][FollowingData["Activity"] == max(FollowingData["Activity"])]
print "The person who is most active that Matt follows is " + (str(most_active.values)[2:-2]) + ", who on average posts " + str(max(FollowingData["Activity"])) + " times a day."