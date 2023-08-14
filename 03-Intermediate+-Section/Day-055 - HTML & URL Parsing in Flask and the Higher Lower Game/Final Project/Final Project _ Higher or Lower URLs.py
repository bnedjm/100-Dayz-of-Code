from flask import Flask
from random import randint

app = Flask(__name__)

GUESS = randint(0,9)

@app.route("/")
def home():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9.</h1>" \
        "<center><img src='https://media.giphy.com/media/grDFHLDd6Bl9vDCr4Z/giphy.gif'></center>"

@app.route("/<int:number>")
def guess(number):
    if number < GUESS:
        return "<h1 style='color: blue; text-align: center'>Too low, get high!</h1>" \
            "<center><img src='https://media.giphy.com/media/WvKGGZkFikKmk/giphy.gif'></center>"
    elif number > GUESS:
        return "<h1 style='color: red; text-align: center'>Too high!</h1>" \
            "<center><img src='https://media.giphy.com/media/21JMq0e5LSUJq/giphy.gif'></center>"
    else:
        return "<h1 style='color: green; text-align: center'>We' chilling, you got it right.</h1>" \
            "<center><img src='https://media.giphy.com/media/1060C3ZvLPEOAM/giphy.gif'></center>"


if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    app.run(debug=True)