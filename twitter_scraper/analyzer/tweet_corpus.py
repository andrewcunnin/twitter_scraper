import json
import nltk
import analyzer.tweet_scrubber as ts
import analyzer.corpus_utils as cu

class TweetCorpus:
	def __init__(self, tweets):
		self.tweets = tweets
		tweets_text = [getattr(tweet, 'text') for tweet in tweets]
		tweets_text = ts.clean_tweets(tweets_text)
		self.text = nltk.word_tokenize('# '+" # \n # ".join(tweets_text) + ' #')
		(self.f_dist, self.f_bigrams, self.p_dist, self.p_bigrams, self.pos) = cu.parse_data(self.text)

	def write_corpus_to_json(self): #writes all tweet_text bodies to json given search terms
		with open('my_tweet_corpus.json', 'w') as outfile:
			json.dump(self.text, outfile)

	def get_p(self, word): # finds probability of word in tweet texts
		return self.p_dist[word]

	def get_p_given(self, prev, word): # finds probability of word given prev
		return self.p_bigrams[prev][word]

	def generate_tweet(self):
		# while character count is less than 280
				# sample word from bigrams starting with '#'
		pass
