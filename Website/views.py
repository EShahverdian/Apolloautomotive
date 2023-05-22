from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # create a blueprint named 'views'


@views.route('/')  # decorator for the home page route
def home():
    return render_template("home.html")  # render the 'home.html' template


@views.route('/logout')  # decorator for the logout route
def logout():
    return render_template('logout.html')  # render the 'logout.html' template


@views.route('/signup')  # decorator for the logout route
def signup():
    return render_template('signup.html')  # render the 'logout.html' template


@views.route('/carlist')  # decorator for the logout route
def carlist():
    return render_template('carlist.html')  # render the 'logout.html' template

@views.route('/login')  # decorator for the logout route
def login():
    return render_template('login.html')  # render the 'login.html' template