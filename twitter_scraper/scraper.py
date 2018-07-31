import system
import re
import json

def cleanText(str):
    regex = re.compile("^(RT)|(@[^\s]*\s?)|(#[^\s]*\s?)|(https://[^\s]*[\s]?)|([^a-z\sA-Z0-9]*)")
    return removeStops(regex.sub('', str).lower())

def removeWord(word, str):
    regex = re.compile("\s([^A-Z|a-z|0-9]*)" + word + "([^A-Z|a-z|0-9]*)\s")
    return regex.sub(' ', str)

def removeStops(str):
    stops = ["a", "also", "an", "and", "as", "at", "be", "but", "by", "can", "could", "do", "for", "from", "go", "have",
             "her", "here", "his", "how", "i", "if", "in", "into", "it", "its", "my", "of", "on", "or", "our", "say", "she",
             "that", "the", "their", "there", "therefore", "they", "this", "these", "those", "through", "to", "until", "we",
             "what", "when", "where", "which", "while", "who", "with", "would", "you", "your"]
    for stop in stops:
        str = removeWord(stop, str)
    return str

def scrapeNoisy(keyTerm, n):
    if(n > 100):
        n = 100
    if(n < 0):
        n = 0;
    tweets = system.api.search(q=keyTerm, count = n)
    return [getattr(tweet, 'text').encode('UTF-8') for tweet in tweets]

def scrape(keyTerm, n):
    tweets = scrapeNoisy(keyTerm, n)
    return [cleanText(tweet) for tweet in tweets]

def getWordFrequencies(str):
    freqs = {}
    strs = str.split()
    for word in strs:
        if(word in freqs):
            freqs[word] += 1
        else:
            freqs[word] = 1
    return freqs

def getRelativeFrequencies(contents):
    rel_freqs = {}
    count = 0
    for key, value in contents.items():
        count += value
    for key, value in contents:
        rel_freqs[key] = float(value/count)

def writeCorpus(keyword_list):
    tweets = []
    for keyWord in keyword_list:
        tweets += system.api.search(q=keyWord, count = 100)
    with open('my_tweet_corpus.json', 'w') as outfile:
        (json.dump(tweet, outfile) for tweet in tweets)

def getCorpus(keyWord):
    tweets = scrape(keyWord, 100)
    if (tweets != None):
        str = ""
        for tweet in tweets:
            str += tweet + " "
        return(str)

#print(getWordFrequencies(cleanText("u'RT u'and \ni, must, 1 say that this is a nice house RT @user #cool https://mywebsite.com haha'", )))