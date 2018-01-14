
from flask import Flask
from flask import render_template

app = Flask(__name__)


""" Web root
"""
@app.route('/')
def root(name=None):
    return render_template('canvas.html', name=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



