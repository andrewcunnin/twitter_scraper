import re
import json
import nltk

stops = ["a", "also", "an", "and", "as", "at", "be", "but", "by", "can", "could", "do", "for", "from", "go", "have",
	 "her", "here", "his", "how", "i", "if", "in", "into", "it", "its", "my", "of", "on", "or", "our", "say", "she",
	 "that", "the", "their", "there", "therefore", "they", "this", "these", "those", "through", "to", "until", "we",
	 "what", "when", "where", "which", "while", "who", "with", "would", "you", "your"]

punctuation = re.compile("[^a-z\sA-Z0-9]*")
tweet_elems = re.compile("^(RT)|(@[^\s]*\s?)|(#[^\s]*\s?)|(https://[^\s]*[\s]?)*")

def remove_tweet_elems(tweet_text): #removes tweet_text elements like hashtags, RTs, and links
	return tweet_elems.sub('', tweet_text);

def remove_punctuation(tweet_text): #removes all punctuation from tweet_text
	return punctuation.sub('', tweet_text);

def remove_word(word, tweet_text): #removes all occurrences of word from tweet_text
	regex = re.compile("\s([^A-Z|a-z|0-9]*)" + word + "([^A-Z|a-z|0-9]*)\s")
	return regex.sub(' ', tweet_text)

def clean_tweet(tweet_text): #cleans tweet text
	return remove_punctuation(remove_tweet_elems(remove_stops(tweet_text))).lower().strip();

def clean_tweets(tweets_text):
	return [clean_tweet(tweet_text) for tweet_text in tweets_text]

def remove_stops(tweet_text): #removes stop words from tweet_texting
	for stop in stops:
		tweet_text = remove_word(stop, tweet_text)
	return tweet_text;

class TweetCorpus:
	def __init__(self, tweets):
		self.tweets = tweets
		tweets_text = [getattr(tweet, 'text') for tweet in tweets]
		tweets_text = clean_tweets(tweets_text)
		self.text = nltk.word_tokenize('# '+" # \n # ".join(tweets_text) + ' #')
		self.fdist = nltk.FreqDist(self.text)
		self.bigrams = nltk.bigrams(self.text)

	def write_corpus_to_json(tweet_texts): #writes all tweet_text bodies to json given search terms
		tweet_texts = clean_tweets(tweet_texts)
		with open('my_tweet_corpus.json', 'w') as outfile:
			(json.dump(tweet, outfile) for tweet in tweet_texts)

	def get_probability(self, word): #finds probability of word in tweet texts
		return self.fdist[word]/float(len(self.text)) #should store distribution as a field for parse objects
