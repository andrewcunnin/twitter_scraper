import tweet_analyzer
import unittest

class TestTweetAnalyzer(unittest.TestCase):
    def setUp(self):
        self.tweets = ["test tweet 123 @user #testing", "a tweet number 2"]

    def test_clean_tweets(self):
        cleaned = tweet_analyzer.clean_tweets(self.tweets)
        self.assertEqual(cleaned[0], "test tweet 123")
        self.assertEqual(cleaned[1], "a tweet number 2")

if __name__ == '__main__':
    unittest.main()
