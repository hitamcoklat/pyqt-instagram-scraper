from twitter_scraper import get_tweets, get_trends, Profile
import json

class TwitterScrape(object):

    def get_tweets(jmlPage = 1):

        data_tweet = []

        for x in range(0, jmlPage):
            for tweet in get_tweets('#bandung', pages=x):
                data_tweet.append(tweet['username'])

        return data_tweet

    def get_trends():
        return get_trends()

    def getProfile(username):
        profile = Profile(username)
        return profile.to_dict()


# print(TwitterScrape.get_trends())
print(TwitterScrape.getProfile('ridwankamil'))
# print(json.dumps(TwitterScrape.get_tweets(jmlPage=2), indent=4))
# print(TwitterScrape.get_tweets())