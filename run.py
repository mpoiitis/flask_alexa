import logging
import twitchapi
from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('IsStreaming', mapping={'name': 'Streamer'})
def IsStreaming(name):
    if(twitchapi.is_online(name)):
        return statement(render_template("nai", Streamer = name))
    else:
        return statement(render_template("psofa", Streamer = name))


@ask.launch
def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)

if __name__ == '__main__':

    app.run(debug=True)
