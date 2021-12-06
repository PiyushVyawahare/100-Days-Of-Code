from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 1 and 9.</h1>" \
           "<br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200 />"


@app.route('/<int:num>')
def guess_num(num):
    if num > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200/>"
    elif num < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200/>"
    else:
        return "<h1 style='color: green'>You guessed it correct. You Found Me!</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200/>"


if __name__ == "__main__":
    app.run(debug=True)
