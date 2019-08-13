import scraper.tweet_system as system

def scrape_text(keyTerm, n=100): #does not parse tweets, term to search by, amount of tweets to scrape
	if(n > 100):
		n = 100
	if(n < 0):
		n = 0;
	tweets = system.api.search(q=keyTerm, count = n)
	return [getattr(tweet, 'text') for tweet in tweets]
