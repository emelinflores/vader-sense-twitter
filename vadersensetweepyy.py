import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv 

# Twitter API configuration
twconfig = {  
    'api_key': "",
    'api_secret': "",
    'access_token': "",
    "access_secret": ""
}

# Tweepy setup
auth = tweepy.OAuthHandler(
    twconfig['api_key'],
    twconfig['api_secret'])

auth.set_access_token(
    twconfig['access_token'],
    twconfig['access_secret'])

tw = tweepy.API(auth)

##Part 1 Data Extraction and Transformation

## Data ETL process starts here / Function to Extract Data 
def extract(query):
    """Returns results from a Twitter search.
    
    Accepts one argument: the query (as a string object) to use to search Twitter."""

    #checks if query is NOT a string
    if not isinstance(query, str):
        return None
    else:
        results = tw.search(query, tweet_mode="extended", count=500)
        return results

#Extracting data with perimeters     
data = extract('"5GCoronavirus" OR "5GVirus" OR "5GMindControl" -filter:retweets -filter:replies lang:en until:2020-04-30')

#Printing the results if needed
#for tweet in data:
#  print(f"\n{tweet.full_text} \n")

#Creating a txt file 
with open('5gtweets.txt', 'w') as myfile:
  for tweet in data:
    myfile.write(f"'{tweet.full_text}' \n")

#Part 2 Data Loading 

#Creating a variable to use sentiment analyzer function
analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(sourcefile):
    with open(sourcefile, 'r') as tweetstxt:
      print("Reading file...\n")
    # Creating a list to read each line of the txt file and append the lines to the list
      tweets = []
      count = 0
      while True: 
        count += 1
        line = tweetstxt.readline() 
        tweets.append(line)
        if not line: 
          break
  
      tweetstxt.close() 

    # Create postive, neutral, and negative lists to append the respective tweets in lists
    pos_tweets = []
    neu_tweets = [] 
    neg_tweets = []
    #Based off of VADER documentation, this is how I would score the tweets
    for sentence in set(tweets):
      if (analyzer.polarity_scores(sentence)['compound']) >= 0.05:
        pos_tweets.append(sentence)
      elif (analyzer.polarity_scores(sentence)['compound']) <= -0.05:
        neg_tweets.append(sentence)
      else:
        neu_tweets.append(sentence)

  #Finding the size of each list 
    lens = [len(pos_tweets), len(neu_tweets), len(neg_tweets)]

    return [pos_tweets, neu_tweets, neg_tweets, lens]

data = sentiment_analysis('5gtweets.txt')

#Creating CSV file to display lists of positive, neutral, and negative tweets and the size of their lists 
with open('tweetanalysis.csv', 'w', newline='') as myfile:
  write = csv.writer(myfile)
  write.writerows(data) 

