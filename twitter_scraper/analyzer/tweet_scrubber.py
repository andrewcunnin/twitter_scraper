import re

stops = ["a", "also", "an", "and", "as", "at", "be", "but", "by", "can", "could", "do", "for", "from", "go", "have",
	 "her", "here", "his", "how", "i", "if", "in", "into", "it", "its", "my", "of", "on", "or", "our", "say", "she",
	 "that", "the", "their", "there", "therefore", "they", "this", "these", "those", "through", "to", "until", "we",
	 "what", "when", "where", "which", "while", "who", "with", "would", "you", "your"]

punctuation = re.compile("[^a-z\sA-Z0-9]*")
tweet_elems = re.compile("^(RT)|(@[^\s]*\s?)|(#[^\s]*\s?)|(https://[^\s]*[\s]?)*")

def remove_tweet_elems(text): #removes text elements like hashtags, RTs, and links
	return tweet_elems.sub('', text);

def remove_punctuation(text): #removes all punctuation from text
	return punctuation.sub('', text);

def remove_word(word, phrase): #removes all occurrences of word from text
	return [w for w in phrase if w != word]

def clean_tweet(text): #cleans tweet text
	return remove_punctuation(remove_tweet_elems(text)).lower().strip();

def clean_tweets(texts):
	return [clean_tweet(text) for text in texts]

def remove_stops(text): #removes stop words from texting
	for stop in stops:
		text = remove_word(stop, text)
	return text;
