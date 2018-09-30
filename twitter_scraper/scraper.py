import system
import re
import json
import nltk

def remove_tweet_elems(str_var): #removes tweet elements like hashtags, RTs, and links
	regex = re.compile("^(RT)|(@[^\s]*\s?)|(#[^\s]*\s?)|(https://[^\s]*[\s]?)*")
	return regex.sub('', str_var);
    
def clean_corpus(str_var): #cleans everything except words and spaces from str_varing
	return remove_punctuation(remove_tweet_elems(remove_stops(str_var))).lower();

def remove_punctuation(str_var): #removes all punctuation from str_varing
	regex = re.compile("[^a-z\sA-Z0-9]*")
	return regex.sub('', str_var);

def remove_word(word, str_var): #removes all occurrences of word from str_varing
	regex = re.compile("\s([^A-Z|a-z|0-9]*)" + word + "([^A-Z|a-z|0-9]*)\s")
	return regex.sub(' ', str_var)

def remove_stops(str_var): #removes stop words from str_varing
	stops = ["a", "also", "an", "and", "as", "at", "be", "but", "by", "can", "could", "do", "for", "from", "go", "have",
	     "her", "here", "his", "how", "i", "if", "in", "into", "it", "its", "my", "of", "on", "or", "our", "say", "she",
	     "that", "the", "their", "there", "therefore", "they", "this", "these", "those", "through", "to", "until", "we",
	     "what", "when", "where", "which", "while", "who", "with", "would", "you", "your"]
	for stop in stops:
		str_var = remove_word(stop, str_var)
	return str_var;

def scrape_noisy(keyTerm, n): #does not parse tweets, term to search by, amount of tweets to scrape
	if(n > 100):
		n = 100
	if(n < 0):
		n = 0;
	tweets = system.api.search(q=keyTerm, count = n)
	return [getattr(tweet, 'text').encode('UTF-8') for tweet in tweets]

def scrape(keyTerm, n): #term to search by, amount of tweets to scrape
    tweets = scrape_noisy(keyTerm, n)
    return [remove_tweet_elems(tweet) for tweet in tweets]

def write_corpus(keyword_list): #writes all tweet bodies to json given search terms
	tweets = []
	for keyWord in keyword_list:
		tweets += system.api.search(q=keyWord, count = 100)
	with open('my_tweet_corpus.json', 'w') as outfile:
		(json.dump(tweet, outfile) for tweet in tweets)

def get_probability(str_var, substring): #finds probability that substr_varing is found in str_varing
	arr = nltk.word_tokenize(str_var)
	fdist = nltk.FreqDist(arr)
	return fdist[substring]/len(arr) #should store distribution as a field for parse objects

def get_corpus(keyWord): #scrapes a default 100 tweets given a search term
	tweets = scrape(keyWord, 100)
	if (tweets != None):
		str_var = ""
		for tweet in tweets:
			str_var += tweet + " "
		return(str_var)
str_var = "hi hi hi this is me ok"
print(str(get_probability(str_var, "hi")))
