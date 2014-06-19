# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template
from models import Members, Events

@app.route('/', methods = ['GET', 'POST'])
def index():
	members = Members.query.all
	return render_template('index.html', members = members)


@app.route('/events')
def events():
	return render_template('events.html')