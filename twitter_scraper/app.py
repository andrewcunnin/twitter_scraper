import scraper.tweet_scraper as tweet_scraper
import analyzer.tweet_analyzer as tweet_analyzer

tweet_texts = tweet_scraper.scrape_text('hello', 100)
corpus = (' ').join(tweet_analyzer.clean_tweets(tweet_texts))
print(corpus)
print(tweet_analyzer.get_probability(corpus, 'hello'))
#scraper.getRelativeFrequencies
