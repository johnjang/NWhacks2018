#! /usr/bin/python

from flask import Flask
from flask import render_template

app = Flask(__name__)


""" Web root
"""
@app.route('/')
    return render_template('canvas.html', name=None)






