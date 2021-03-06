from werkzeug.contrib.cache import SimpleCache
from util.insta import MyInstagram
from util.quotes import MyQuotes
from util.projects import MyProjects
from util.twitter import MyTwitter

""" Various contents of the application """

# We make one cache that will store everything.
# Distinct shorter cache for tweets
cache = SimpleCache(default_timeout=30 * 24 * 60 * 60) # 30 days
cache_twitter = SimpleCache(default_timeout=60 * 60) # 1h

def cached_instagram():
    """ Caching handler for MyInstagram """ 
    ig = cache.get('instagram')
    if ig is None:
        print "Re-caching Instagram.."
        ig = MyInstagram()
        cache.set('instagram', ig)
    return ig

def cached_quotes():
    """ Caching handler for MyQuotes """
    q = cache.get('quotes')
    if q is None:
        print "Re-caching quotes.."
        q = MyQuotes()
        cache.set('quotes', q)
    return q

def cached_projects():
    """ Caching handler for MyProjects """
    p = cache.get('projects')
    if p is None:
        print "Re-caching projects.."
        p = MyProjects()
        cache.set('projects', p)
    return p

def cached_tweets():
    """ Caching handler for MyTwitter """
    tw = cache_twitter.get('tweets')
    if tw is None:
        print "Re-chacing tweets.."
        tw = MyTwitter()
        cache_twitter.set('tweets', tw)
    return tw

