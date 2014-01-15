from flask import Flask, render_template
from pnext import app
import contents

@app.route('/')
def index():
    # Content
    ig = contents.cached_instagram() # Instagram backgrounds
    q = contents.cached_quotes() # Quotes

    images = [ ig.get_random_img() for i in xrange(4)] # 4 sections
    quote = q.get_random_quote()
    return render_template('index.htm', backgrounds=images, quote=quote)

@app.before_request
def before_request():
    pass
