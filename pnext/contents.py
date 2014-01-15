from werkzeug.contrib.cache import SimpleCache
from util.ig import MyInstagram
from util.quotes import MyQuotes

""" Various contents of the application """

# We make one cache that will store everything
# TODO Better caching management (manual, when a change is detected, etc.)
cache = SimpleCache(default_timeout=24 * 60 * 60) # 24h

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
