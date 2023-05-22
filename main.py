from Website import create_app  # import the create_app function from the Website module

app = create_app()  # create a Flask application using the create_app function
if __name__ == '__main__':
    app.run(debug=True)  # start the Flask application and run it in debug mode if this file is being run as the main
    # program
