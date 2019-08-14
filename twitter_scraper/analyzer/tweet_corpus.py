import json
import nltk
import analyzer.tweet_scrubber as ts

class TweetCorpus:
	def __init__(self, tweets):
		self.tweets = tweets
		tweets_text = [getattr(tweet, 'text') for tweet in tweets]
		tweets_text = ts.clean_tweets(tweets_text)
		self.text = nltk.word_tokenize('# '+" # \n # ".join(tweets_text) + ' #')
		self.fdist = nltk.FreqDist(self.text)
		self.bigrams = list(nltk.bigrams(self.text))
		self.fdist_bigrams = nltk.FreqDist(self.bigrams)

	def write_corpus_to_json(self): #writes all tweet_text bodies to json given search terms
		with open('my_tweet_corpus.json', 'w') as outfile:
			json.dump(self.text, outfile)

	def get_p_word(self, word): #finds probability of word in tweet texts
		return self.fdist[word]/float(len(self.text)) #should store distribution as a field for parse objects

	def get_p_bigram(self, prev, word):
		return self.fdist_bigrams[(prev, word)]/float(len(self.bigrams))
