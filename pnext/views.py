from flask import Flask, render_template
from pnext import app

@app.route('/')
def index():
    return render_template('index.htm')
