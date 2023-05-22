from . import db  # Import db from the current package
from flask_login import UserMixin  # Import UserMixin from flask_login


# from sqlalchemy.sql import func  # Import func from sqlalchemy.sql

class Car(db.Model):  # Define the Car model that extends db.Model
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as an Integer primary key
    make = db.Column(db.String(50), nullable=False)  # Define the make column as a non-nullable String
    model = db.Column(db.String(50), nullable=False)  # Define the model column as a non-nullable String
    year = db.Column(db.Integer, nullable=False)  # Define the year column as a non-nullable Integer
    price = db.Column(db.Float, nullable=False)  # Define the price column as a non-nullable Float
    image_filename = db.Column(db.String(100), nullable=True)  # Define the image_filename column as a nullable String


class User(db.Model, UserMixin):  # Define the User model that extends db.Model and UserMixin
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as an Integer primary key
    email = db.Column(db.String(150), unique=True)  # Define the email column as a unique String
    password = db.Column(db.String(150))  # Define the password column as a String
    firstName = db.Column(db.String(150))  # Define the firstName column as a String
    lastName = db.Column(db.String(150))  # Define the lastName column as a String
    confirmPassword = db.Column(db.String(150))  # Define the confirmPassword column as a String
