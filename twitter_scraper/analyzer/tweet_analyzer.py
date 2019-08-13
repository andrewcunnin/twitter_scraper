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

def clean_tweets(tweet_texts):
	return [clean_tweet(tweet_text) for tweet_text in tweet_texts]

def remove_stops(tweet_text): #removes stop words from tweet_texting
	for stop in stops:
		tweet_text = remove_word(stop, tweet_text)
	return tweet_text;

def write_corpus_to_json(tweet_texts): #writes all tweet_text bodies to json given search terms
	tweet_texts = clean_tweets(tweet_texts)
	with open('my_tweet_corpus.json', 'w') as outfile:
		(json.dump(tweet, outfile) for tweet in tweet_texts)

#TODO - make corpus object so that fdist can be defined for full object
def get_probability(tweet_text, word): #finds frequency of word in tweet texts
	arr = nltk.word_tokenize(tweet_text)
	fdist = nltk.FreqDist(arr)
	return fdist[word]/float(len(arr)) #should store distribution as a field for parse objects
