import json
import os
import re
import sqlite3


def loadtweets(file):
    tweetstring = []

    with open(file) as tweetfile:
        for line in tweetfile:
            tweetstring.append(json.loads(line)["text"])

    return tweetstring


def searchtweets(tweets, term):
    result = []
    for tweet in tweets:
        match = re.search("(.+)" + term + "(.+)", tweet)
        if match is not None:
            result.append(tweet)

    return result


def counttweets(sortedtweets):
    return len(sortedtweets)
