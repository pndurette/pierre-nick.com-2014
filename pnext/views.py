from flask import Flask, render_template
from pnext import app
import contents

@app.route('/')
def index():
    # Content: Instagram backgrounds
    ig = contents.cached_instagram()
    images = [ ig.get_random_img()['img'] for i in xrange(4)]
    return render_template('index.htm', backgrounds=images)

@app.before_request
def before_request():
    pass
