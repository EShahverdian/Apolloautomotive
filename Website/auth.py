from flask import Blueprint, render_template, request, flash  # Import Blueprint, render_template, request, and flash from Flask
from Website.models import User, Car  # Import User and Car models from Website.models
from Website import db  # Import db from Website

auth = Blueprint('auth', __name__)  # Create a new Blueprint named 'auth'


@auth.route('/login', methods=['GET', 'POST'])  # Route decorator for the login page
def login():
    data = request.form  # Get the form data from the request

    if request.method == 'POST':
        email = request.form.get('email')  # Get the email from the form data
        password = request.form.get('password')  # Get the password from the form data

        if len(email) < 4:
            flash('Email not valid.', category='error')  # Flash an error message if the email is not valid
        elif len(password) < 6:
            flash('Passwords needs to be more than 5 characters.', category='error')  # Flash an error message if the password is too short
        else:
            flash('Login successful!', category='success')  # Flash a success message if the login is successful

    print(data)
    return render_template("login.html")  # Return the rendered HTML content for the login page


@auth.route('/logout')  # Route decorator for the logout page
def logout():
    return "<p>Logout</p>"  # Return the HTML content for the logout page


@auth.route('/signup', methods=['GET', 'POST'])  # Route decorator for the sign-up page
def sign_up():
    datasignup = request.form  # Get the form data from the request

    if request.method == 'POST':
        email = request.form.get('email')  # Get the email from the form data
        firstName = request.form.get('firstName')  # Get the first name from the form data
        lastName = request.form.get('lastName')  # Get the last name from the form data
        password = request.form.get('password')  # Get the password from the form data
        confirmPassword = request.form.get('confirmPassword')  # Get the confirmed password from the form data

        if len(email) < 4:
            flash('Email not valid.', category='error')  # Flash an error message if the email is not valid
        elif len(firstName) < 2:
            flash('Please enter more than 2 characters for the first name.', category='error')  # Flash an error message if the first name is too short
        elif len(lastName) < 2:
            flash('Please enter more than 2 characters for the last name.', category='error')  # Flash an error message if the last name is too short
        elif password != confirmPassword:
            flash('Passwords do not match.', category='error')  # Flash an error message if the passwords do not match
        elif len(password) < 6:
            flash('Passwords needs to be more than 5 characters.', category='error')  # Flash an error message if the password is too short
        else:
            # db.new_user = User(email=email, firstName=firstName, password=password, lastName=lastName, confirmPassword=confirmPassword)
            # db.session.add(db.new_user)
            # db.session.commit()

            flash('Sign-Up successful!', category='success')  # Flash a success message if the sign-up is successful

    print(datasignup)
    return render_template("signup.html")  # Return the rendered HTML
