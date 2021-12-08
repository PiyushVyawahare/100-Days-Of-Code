import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template("index.html", all_blogs=all_blogs)


@app.route('/post/<int:index>')
def show_post(index):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template("post.html", blog=all_blogs[index-1])


if __name__ == "__main__":
    app.run(debug=True)

