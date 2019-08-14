import scraper.tweet_system as system

def scrape_text(keyTerm, n): #does not parse tweets, term to search by, amount of tweets to scrape
	#TODO - add rate limiting
	return system.api.search(q=keyTerm, count = n)
