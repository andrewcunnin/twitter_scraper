import scraper

text = raw_input("enter keyword: ")
print(scraper.getWordFrequencies(scraper.getCorpus('rubarb')))
#scraper.getRelativeFrequencies