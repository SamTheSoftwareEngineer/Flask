# Import neccesary packages
from flask import Flask, render_template, request
from flask import DebugToolbarExtension
from stories import story

# Creates instance of flask application
app = Flask(__name__)
# Secret key sued to securely sign cookies and other data
app.config['SECRET_KEY'] = "stewart"
# Assigning debugger tool
debug = DebugToolbarExtension(app)

# Defines a flask route for the url path /form
@app.route('/form')
def form_page():
    # Save story prompts to a variable to access 
    prompts = story.prompts
    # Renders the form file to display to the user 
    return render_template("form.html", prompts=prompts)

# Same logic as previous route
@app.route('/story')
def show_stories():
    text = story.generate(request.args)
    return render_template("story.html", text = text)
