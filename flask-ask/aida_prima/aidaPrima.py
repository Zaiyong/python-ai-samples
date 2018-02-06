import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import time,json

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

@ask.intent('ExcursionIntent',convert={'the_day': str})
def getExcursion(the_day):
    excursion = json.load(open('excursion.json'))
    print(excursion)
    excursion_msg=render_template('excursion', excursion=excursion[the_day],the_day=the_day)
    return statement(excursion_msg)

@ask.intent('RestaurantOpenTimeIntent',convert={'restaurant': str})
def getOpenTime(restaurant):
    open_time = json.load(open('restaurant_open.json'))
    print(open_time)
    open_time_msg=render_template('open_time_restaurant',
                                    restaurant=restaurant,
                                    open=open_time[restaurant]['open'],
                                    close=open_time[restaurant]['close'])
    return statement(open_time_msg)



if __name__ == '__main__':
    app.run()
