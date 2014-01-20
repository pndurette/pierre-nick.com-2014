import os, json, random

class MyQuotes:
    QUOTES_FILE = os.path.join(os.path.dirname(__file__), "../data/quotes.json")
    
    def __init__(self):
        self._quotes_list = json.load(open(MyQuotes.QUOTES_FILE))['quotes']
    
    def get_random_quote(self):
        return random.choice(self._quotes_list)
