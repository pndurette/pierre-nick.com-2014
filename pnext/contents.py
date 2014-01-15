from werkzeug.contrib.cache import SimpleCache
from util.ig import MyInstagram

""" Various contents of the application """

# We make one cache that will store everything
cache = SimpleCache()

def cached_instagram():
    """ Caching handler for MyInstagram """ 
    ig = cache.get('instagram')
    if ig is None:
        ig = MyInstagram()
        cache.set('instagrams', ig, timeout=5 * 60)
    return ig
