import tweetcounter

def test_loadtweets(filename = 'docs/tweets.json'):
    file = tweetcounter.loadtweets(filename)
    assert len(file) == 10972

def test_searchtweets(filename = 'docs/tweets.json', term = 'food'):
    file = tweetcounter.loadtweets(filename)
    tweets = tweetcounter.searchtweets(file, term)

    assert "I would get food poisoning when I'm in Vegas. #FML" in tweets


def test_counttweets(filename = 'docs/tweets.json', term = 'vomit'):
    file = tweetcounter.loadtweets(filename)
    tweets = tweetcounter.searchtweets(file, term)
    count = tweetcounter.counttweets(tweets)

    assert count == 7142
