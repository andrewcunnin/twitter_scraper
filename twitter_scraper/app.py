import scraper.tweet_scraper as tweet_scraper
import analyzer.tweet_analyzer as tweet_analyzer

tweets = tweet_scraper.scrape_text('hello', 100)
my_analyzer = tweet_analyzer.TweetCorpus(tweets)
print(my_analyzer.get_probability('hello'))
#scraper.getRelativeFrequencies
