# Import the Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


# Define a function to create a Flask app instance
def create_app():
    # Create a Flask app instance with the name of this module
    app = Flask(__name__)

    # Set a secret key for the app to use for secure sessions
    app.config['SECRET_KEY'] = 'sleopxlvkexqkmansxjf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import the views blueprint from the views module
    # Import the auth blueprint from the auth module
    from .views import views
    from .auth import auth

    # Register the views blueprint with the app, with a URL prefix of "/"
    # Register the auth blueprint with the app, with a URL prefix of "/"
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from Website import models

    # Return the app instance
    return app


#def create_database(app):
    #if not path.exists('Website/' + DB_NAME):
        # Create the database tables
        #db.create_all(app=app)
        #print('Database created!')
