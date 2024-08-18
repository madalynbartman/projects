from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/") # endpoint
def index():
    return render_template("index.html", launches=launches)

@app.template_filter("date_only")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ") # strip off the time and return the date
    return date_object.date()

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches" # get the launch data
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
    
def categorize_launches(launches): # replaced x with launch
    sucessful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
        "sucessful": sucessful,
        "failed": failed,
        "upcoming": upcoming
    }

launches = categorize_launches(fetch_spacex_launches())

if __name__=="__main__": # ensures you ran this python file directly, not if its used by a diff python file
    app.run(debug=True)
