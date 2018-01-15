from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/signup")
def signup():
     return render_template('signup.html')

