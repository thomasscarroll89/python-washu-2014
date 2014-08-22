#Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('jooBNWU5FQzoGWkswSD7ceJoV', 'fiG18cYY8892BBM1xpLibXtX0gp4SGx1nhP4C8tp6lZMDYp65I')
auth.set_access_token('2745400866-0v7E4PswPJo8TCmWG13KjLNW9rvy9rN9V8zQZqX', 'GY1DOlnPR84prNyOhRM9ysHlkdUcEwn8WUbYzCfKrKKrN')    
api = tweepy.API(auth)

#See rate limit
api.rate_limit_status()

#Get all tweets, https://dev.twitter.com/docs/api/1/get/statuses/public_timeline
public_tweets = api.public_timeline()
for t in public_tweets:
  #Note I am handling UTF encoded strings so I convert them to ASCII-compatible for my mac
  print "{0}: {1}".format(t.user.screen_name.encode('ascii', 'ignore'), t.text.encode('ascii', 'ignore'))

#Get some users
mike_ward = api.get_user('3876')

#How many favorites does he have?
mike_ward.favourites_count

#Who does Mike follow?
mikes_friends = api.friends(id=mike_ward.screen_name)
for f in mikes_friends:
  #Note I am handling UTF encoded strings so I convert them to ASCII-compatible for my mac
  print "{0}".format(f.screen_name.encode('ascii', 'ignore'))
