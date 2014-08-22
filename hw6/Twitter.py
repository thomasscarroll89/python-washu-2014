import tweepy
import time
import csv 
import pandas 
import sys

auth = tweepy.OAuthHandler('jooBNWU5FQzoGWkswSD7ceJoV', 'fiG18cYY8892BBM1xpLibXtX0gp4SGx1nhP4C8tp6lZMDYp65I')
auth.set_access_token('2745400866-0v7E4PswPJo8TCmWG13KjLNW9rvy9rN9V8zQZqX', 'GY1DOlnPR84prNyOhRM9ysHlkdUcEwn8WUbYzCfKrKKrN')    
api = tweepy.API(auth)

api.rate_limit_status()

#Make an empty .csv file to story everything into
headers = ["UserName", "Followers", "Following", "TotalTweets", "StartDate"]
filename = "twitter-activity.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

matt_dickenson = api.get_user("202203453")
for user in tweepy.Cursor(api.followers, screen_name="matt_dickenson").items():
	time.sleep(5)
	observation = [user.screen_name, user.followers_count, user.friends_count, user.statuses_count, user.created_at]
	csvwriter.writerow(observation)
	
readFile.close()

#Make an empty .csv file to story everything into
headers = ["UserName", "Followers", "Following", "TotalTweets", "StartDate"]
filename = "twitter-activity2.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

for user in tweepy.Cursor(api.friends, screen_name="matt_dickenson").items():
	time.sleep(5)
	observation = [user.screen_name, user.followers_count, user.friends_count, user.statuses_count, user.created_at]
	csvwriter.writerow(observation)
	
readFile.close()

print pandas.read_csv("twitter-activity.csv")
print pandas.read_csv("twitter-activity2.csv")