from flask import Flask
from flask import render_template as rt

import requests
import json
import warnings

response = requests.get("https://api.openbrewerydb.org/v1/breweries")
data = json.loads(response.text)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Joseph Anderson")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", breweries=data)

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html")

@app.route("/about")
def about():
    return rt("about.html")

if __name__ == "__main__":
    app.run(debug=True)