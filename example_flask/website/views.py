from flask import render_template, abort, Response, send_file
from website import app, db
from .models import Page, Tag, Person, Address, Queries


@app.route('/')
def index():
    return render_template('index.html', random_pages=Queries.random(Page, 10))
