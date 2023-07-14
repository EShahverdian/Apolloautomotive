from flask import Blueprint, render_template
import mysql.connector

import mysql.connector
from mysql.connector import Error

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


@views.route('/carlist')
def carlist():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Demigod808!',
            port='3306',
            database='apolloautomotive',
        )

        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM Vehicle')
        vehicles = mycursor.fetchall()

        for vehicle in vehicles:
            print(vehicle)

        mycursor.execute('SELECT * FROM Customer')
        customers = mycursor.fetchall()

        for customer in customers:
            print(customer)

        return render_template('carlist.html', vehicles=vehicles, customers=customers)

    except Error as e:
        print("Error connecting to the database:", e)

    return render_template('carlist.html')

@views.route('/login')  # decorator for the logout route
def login():
    return render_template('login.html')  # render the 'login.html' template
