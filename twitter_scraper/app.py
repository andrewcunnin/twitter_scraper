import scraper.tweet_scraper as tweet_scraper
import analyzer.tweet_corpus as tweet_corpus

tweets = tweet_scraper.scrape_text('hello', 100)
tweet_corpus = tweet_corpus.TweetCorpus(tweets)
print(tweet_corpus.text)
print(tweet_corpus.get_p_word('hello'))
print(tweet_corpus.get_p_bigram('#', '#'))
#scraper.getRelativeFrequencies
