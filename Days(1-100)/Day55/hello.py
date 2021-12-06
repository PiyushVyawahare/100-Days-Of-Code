from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph<p>" \
           "<img src='https://media.giphy.com/media/C1m9MPACd6Nk4/giphy.gif' width=200/>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello! there {name}, you are {number} year old."


if __name__ == "__main__":
    app.run(debug=True)
