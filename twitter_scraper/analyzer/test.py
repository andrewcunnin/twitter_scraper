import tweet_scrubber
import unittest
import nltk

class TestTweetAnalyzer(unittest.TestCase):
    def setUp(self):
        self.tweets = ["test tweet 123 @user #testing", "the a tweet of the number 2"]

    def test_clean_tweets(self):
        cleaned = tweet_scrubber.clean_tweets(self.tweets)
        self.assertEqual(cleaned[0], "test tweet 123")
        self.assertEqual(cleaned[1], "the a tweet of the number 2")

    def test_remove_stops(self):
        phrase = nltk.word_tokenize(self.tweets[1])
        cleaned = tweet_scrubber.remove_stops(phrase)
        self.assertEqual(cleaned, ["tweet", "number", "2"])

if __name__ == '__main__':
    unittest.main()
