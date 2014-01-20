import os
from datetime import datetime
from twython import Twython

class MyTwitter:
    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    DEFAULT_GET = 10
    T_URL = "https://www.twitter.com" 
    ME = "PierreNick"

    def __init__(self):
        self._api = Twython(MyTwitter.APP_KEY, MyTwitter.APP_SECRET, MyTwitter.OAUTH_TOKEN, MyTwitter.OAUTH_TOKEN_SECRET)
        self._tweets = self._load_my_tweets(count=MyTwitter.DEFAULT_GET)

    def _load_my_tweets(self, count):
        """ Loads a number of tweets from the API """
        return self._api.get_user_timeline(screen_name=MyTwitter.ME, count=count)

    def get_tweets(self, count):
        """ Returns a list of dicts of format: """
        """ {'html': <the tweet html with urls and user names linked>, 'created_at': <created at>, "tweet_url": <url>} """
        raw_tweets = self._tweets[0:count]
        new_tweets = []
        for t in raw_tweets:
            tweet = t['text']

            # When we add characters to the string, we must add them twitter's indices
            # and take it into account
            shift = 0

            # Link to user mentions
            # ex: [{u'id': 89905959, u'indices': [0, 9], u'id_str': u'89905959', u'screen_name': u'DBZNappa', u'name': u'Nappa'}]
            ums = t['entities']['user_mentions']
            if ums:
                for um in ums:
                    before = "<a href='%s/%s'>" % (MyTwitter.T_URL, um['screen_name'])
                    after = "</a>"
                    tweet = self._wrap(before, after, tweet, [i + shift for i in um['indices']])
                    shift = shift + len(before) + len(after) 

            # Link the hashtags (search)
            # ex: u'hashtags': [{u'indices': [91, 100], u'text': u'Congrats'}]
            #hashtags = t['entities']['hashtags']
            #if hashtags:
            #    for h in hashtags:
            #        before = "<a href='%s/search?q=%s'>" % (MyTwitter.T_URL, h['text'])
            #        after = "</a>"
            #        tweet = self._wrap(before, after, tweet, [i + shift for i in h['indices']])
            #        shift = shift + len(before) + len(after) 

            # Link to URLs  
            # [{u'url': u'http://t.co/d7nykKVGMa', u'indices': [80, 102], u'expanded_url': u'http://instagram.com/p/jVQCvUQWbB/', u'display_url': u'instagram.com/p/jVQCvUQWbB/'}]}
            urls = t['entities']['urls']
            if urls:
                for url in urls:
                    before = "<a href='%s'>" % url['url']
                    after = "</a>"
                    tweet = self._wrap(before, after, tweet, [i + shift for i in url['indices']])
                    shift = shift + len(before) + len(after)

            # Convert the created_at time/date to Python datetime
            # Ex: Tue Mar 29 08:11:25 +0000 2011
            dt = datetime.strptime(t['created_at'],'%a %b %d %H:%M:%S +0000 %Y')

            new_tweets.append({'html': tweet, 'created_at': dt, 'tweet_url': 'https://twitter.com/%s/status/%s' % (MyTwitter.ME, t['id_str'])})
        return new_tweets

    def _wrap(self, before, after, a_string, indices):
        """ Wrap the part of 'a_string' between 'indices' between 'before' and 'after' """
        """ ex.: _wrap("<this>", "<that>", [2,5], "This is a test") returns "Thi<this>s i<that>s a test"  """""
        """ indices, ex.: [0,2] """
        
        start = a_string[0:indices[0]]
        middle = a_string[indices[0]:indices[1]]
        end = a_string[indices[1]:]
        return start + before + middle + after + end
        
         
