import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

import time
app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent('AskTimeIntent')
def theTime():
    now=time.localtime()
    time_msg=render_template('time', hours=now.tm_hour,minutes=now.tm_min)
    return statement(time_msg)

@ask.intent('AllRestaurantsIntent')
def listRestaurants():
    restaurants=[line.strip() for line in open('restaurants.txt').readlines()]
    restaurants_msg=render_template('restaurants', restaurants=restaurants)
    return statement(restaurants_msg)

if __name__ == '__main__':
    app.run()