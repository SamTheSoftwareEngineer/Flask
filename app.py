# Neccesary to start a server. Think of it like the boiler plate code in HTML.
from flask import Flask

app = Flask(__name__)

# # Enviromental variable --> only available while the program is running 
# FLASK_APP = myapp.py 

# Adding routes --> mapping of a url to some functionality in the application
# /dogs, /login --> add routes


# Creates HTTP response
# @classemethod(decorator)
@app.route('/hello')
def say_hello():
    return "hello there"

@app.route('/goodbye')
def say_bye():
    return "bye!"

# Can also respond with HTML
# @app.route('/hello')
# def say_hello():
#     html = """
#     <html>
#         <body>
#             <h1> Hello! </h1>
#             ...

@app.route('/')
def home_page():
     html = ""
#     <html>
#         <body>
# #             <h1> Home Page </h1>
#                 <p> Welcome to my simple home page </p>
#                 <a href = "/hello">Go to home page </a>
#           ...
