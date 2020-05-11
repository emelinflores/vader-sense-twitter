# How Do Twitter Users Feel About 5G Coronavirus Conspiracy theories? 

My question will be investigating the sentiment towards the [5G Coronavirus conspiracy theories](https://www.vox.com/recode/2020/4/24/21231085/coronavirus-5g-conspiracy-theory-covid-facebook-youtube). Sentiment analysis is Sentiment Analysis, or [Opinion Mining](https://searchbusinessanalytics.techtarget.com/definition/opinion-mining-sentiment-mining), is a sub-field of [Natural Language Processing (NLP)](https://en.wikipedia.org/wiki/Natural_language_processing) that tries to identify and extract opinions within a given text. The aim of sentiment analysis is to gauge the attitude, sentiments, evaluations, attitudes and emotions of a speaker/writer based on the computational treatment of subjectivity in a text. I will extract data from the [Twitter/Tweepy API](https://docs.tweepy.org/en/latest/). This API provides data about tweets posted by users. I will extract trending hashtags like "#5GCoronavirus", "5GVirus", "5GMindControl" and only looking at tweets posted by users. I will not be collecting any retweets or replies. The tweets will be collected in English only. Finally, I will be collecting 500 tweets from 04/30/2020. I will be using VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to draw analysis. I will be using VADER because it is a is a lexicon and rule-based sentiment analysis tool that is  specifically attuned to sentiments expressed in social media.


## Walkthrough

Here is a walkthrough of my code segment by segment. The first thing I did was import the packages I will be using in my program. 

 - Tweepy : I imported Tweepy because I will be using Twitter to extract data from. 
 - VADER Sentiment: I will be using VADER as my sentiment analysis tool 
 - CSV : I will be writing into a CSV file to display my results

The Twitter API configuration and setup can be found [here.](https://docs.tweepy.org/en/latest/getting_started.html) 

![](https://i.ibb.co/mzg0Cvq/intro2.png)

The next segment of code is a function to extract Twitter data. The function results from a Twitter search and accepts on argument which is the query. In the function, if the query is not a string, it will not return anything. When I run this function and I give it one query, it will give me the full tweet indicated by *tweet_mode="extended"* and it will give me 500 tweets indicated by *count=500.*

The last line, I am creating the variable *data* that calls the function *extract* to look for tweets with the hashtags *#5GCoronavirus* or *#5GVirus* or *5GMindControl.* I am using the boolean operator *OR* to give the max amount of results. The next thing I am indicating by my query is that I am filtering retweets and replies. I am only looking for tweets written in English and I am only looking for tweets on 4/30/2020. 

![](https://i.ibb.co/K0byjcC/carbon.png)

After I've extracted the data that I need, I will take the tweets and create a text file named *5gtweets.txt* that only has the full text tweets. 

![](https://i.ibb.co/wJ7vGBT/txt.png)

To analyze the tweets, I created a function with the intention to count how many positive, neutral, and negative tweets there are and to append them to their respective lists. 

At the top of the function, I am creating the variable *analyzer* to use in my function. It is a style preference. The first part of my function is opening the text file I created. I want to read the text file line by line. I create an empty list named *tweets* and create a counter to compliment my while loop to iterate through the text file. My while loop states that I will read the lines one by one and append each line to the list *tweets* and when I reach an object that is not a line, the loop breaks. The text file closes and I am done with reading and appending the tweets to my list.

![](https://i.ibb.co/9rrd33Y/function1.png)

The second part of this function is categorizing the tweets into postive, neutral, and negative lists. First I create empty lists for postive, neutral, and negative tweets. When I am iterating through each tweet or *sentence* I am checking the VADER polarity score. According to the [VADER github page](https://github.com/cjhutto/vaderSentiment#about-the-scoring), this is how tweets are categorized as positive, neutral, and negative:

![](https://i.ibb.co/KqLJN8S/Screen-Shot-2020-05-02-at-9-30-35-PM.png)

I then created a list of the lengths of each list. I will be using these lengths for my results. Finally, my function will return the list for postive tweets, neutral tweets, negative tweets, and the lengths of each list. 

![](https://i.ibb.co/VMFYLcH/functino3.png)

The final segment of my code is that I created a variable *data* that called to the function *sentiment_analysis* to read and cateorize the contents of *5gtweets.txt* The last piece is creating a CSV file titled *tweetanalysis.csv* that will show all the postive, neutral, and negative tweets in their own row so if someone were curious to see what VADER categorized as a positive, neutral, or negative tweet, it would be acessible. Finally, it will display a numeric value of how many tweets were positive, neutral, and negative.
![](https://i.ibb.co/M7JtLgd/csv.png)
## Summary of Results 

I could've created a chart with excel but I used meta-chart.com to upload my CSV file and create this chart. The results only counted 245 tweets out of 500 but they do show that the overall sentiment from tweets are neutral. They also show the second highest category of tweets are negative. This could be valuable information for intelligence angencies or anyone curious about how conspiracy theories are interrpted online and their overall sentiment over users.

![](https://i.ibb.co/tCBFggD/meta-chart.png)

## What To Do Next If This Were a Real-World Project

What I would do next is this were a real-world project is to find a better sentiment analysis tool to analyse tweets a better tools to sparse data from Twitter. In addition, I would try to look for data that covers more than one day because articles suggests that the height of the 5g Coronavirus conspiracy theories started at the beginning of April and I am only allowed to collect data from the end of April. 

## Script

``` python
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

	if  not  isinstance(query, str):
		return  None
	else:
		results = tw.search(query, tweet_mode="extended", count=500)

	return results

#Extracting data with perimeters

data = extract('"5GCoronavirus" OR "5GVirus" OR "5GMindControl" -filter:retweets -filter:replies lang:en until:2020-04-30')

#Creating a txt file
with  open('5gtweets.txt', 'w') as myfile:
	for tweet in data:
		myfile.write(f"'{tweet.full_text}' \n")
		
#Part 2 Data Loading

#Creating a variable to use sentiment analyzer function

analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(sourcefile):
	with  open(sourcefile, 'r') as tweetstxt:
		print("Reading file...\n")

# Creating a list to read each line of the txt file and append the lines to the list
		tweets = []
		count = 0
		while  True:
			count += 1
			line = tweetstxt.readline()
			tweets.append(line)
			if  not line:
				break
		tweetstxt.close()

# Create postive, neutral, and negative lists to append the respective tweets in lists

	pos_tweets = []
	neu_tweets = []
	neg_tweets = []

#Based off of VADER documentation, this is how I would score the tweets

	for sentence in  set(tweets):
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

with  open('tweetanalysis.csv', 'w', newline='') as myfile:
	write = csv.writer(myfile)
	write.writerows(data)

```

