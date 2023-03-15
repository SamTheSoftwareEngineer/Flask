from flask import Flask, redirect, url_for, render_template # Need to import flask in every flask application

# sets this file as the main file
app = Flask(__name__) 

# Defines route for home page, / is the convention for home pages
@app.route("/") 
def home():
    # set content block to read testing and renders the index files as a template 
    return render_template("index.html", content="Testing")
# def home(name):
    # Render created HTML file with name var set to name passed in 
    # return render_template("index.html", name=name, number=2)

# Will pass whatever value to the function
# @app.route("/<name>") 
# def user(name):
#     return f"Hello {name}!"

# Redirect to specific functions that take arguments 
# This next funxtion will handle redirects back to home page
# @app.route("/admin")
# def admin():
#     # return redirect(url_for("home"))
#     return redirect(url_for("user", name="admin"))

# Needed to have the app run on the page 
if __name__ == "__main__": 
    app.run()
    