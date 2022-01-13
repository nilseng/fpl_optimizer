from flask import Flask, redirect, url_for
from markupsafe import escape
from requests import get

from Person import Person
from Coach import Coach
from Player import Player

app = Flask(__name__)

app_name = "Fantasy Premier League Optimizer"

vardy = Player("James Vardy", 10, 70)
print(vardy.name, vardy.weight, vardy.age, "type:", type(vardy))

gerrard = Coach("Stevee G", 50, 80)
print(gerrard, gerrard.team)

@app.route("/")
def landing():
    return f"""<div>
    <h1>{escape(app_name)}</h1>
    <h5>Adjust parameters and generate the optimal Fantasy Premier League team</h5>
    </div>"""

@app.route("/welcome")
def welcome():
    return "<p>Welcome!</p>"

@app.route("/profile/<username>")
def profile(username):
    return f"Hello, {escape(username)}!"

@app.route("/<path:rest>")
def not_found(rest):  
    return redirect("/")

@app.route("/bootstrap-static")
def bootstrap_static():
    data = get("https://fantasy.premierleague.com/api/bootstrap-static/").content
    return data