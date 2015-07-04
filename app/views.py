__author__ = 'jackgolding'

from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hey Govhack'