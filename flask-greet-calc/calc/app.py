# Put your app in here.
from flask import Flask, request
from operations import add ,sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    
    return str(result)

@app.route("/subtract")
def do_subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    
    return str(result)

@app.route("/multiply")
def do_multiplication():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    
    return str(result)

@app.route("/division")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    
    return str(result)
