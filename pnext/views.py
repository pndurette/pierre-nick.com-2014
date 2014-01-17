from flask import Flask, render_template
from pnext import app
import contents

@app.route('/')
def index():
    # Content
    ig = contents.cached_instagram() # Instagram backgrounds
    q = contents.cached_quotes() # Quotes
    p = contents.cached_projects() # Projects

    images = ig.get_random_img_list_of_size(4) # 4 sections
    quote = q.get_random_quote()
    projects = p.get_projects()
    return render_template('index.htm', backgrounds=images, quote=quote, projects=projects)

@app.before_request
def before_request():
    pass
