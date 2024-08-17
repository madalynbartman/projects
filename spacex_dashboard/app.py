from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/") # endpoint
def index():
    return "Hello world!"

if __name__=="__main__": # ensures you ran this python file directly, not if its used by a diff python file
    app.run(debug=True)