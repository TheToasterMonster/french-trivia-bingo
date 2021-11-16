from flask import Flask, redirect, render_template, request
from datetime import datetime
import csv
import random

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# get questions from csv file
with open("questions.csv") as file:
    qbank = list(csv.DictReader(file))
qs = qbank.copy()
past = []
# set random seed
random.seed(datetime.now())

def cleargame():
    """resets game"""
    global qs
    qs = qbank.copy()
    past.clear()
    return


@app.route("/", methods=["GET", "POST"])
def index():
    """Show button to start a game"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        cleargame()
        return redirect("/game")


@app.route("/game", methods=["GET", "POST"])
def game():
    """starts displaying bingo questions"""
    if request.method == "GET":
        if len(qs) == 0:
            return redirect("/")
        num = random.randint(0, len(qs) - 1)
        past.append(qs.pop(num))
        return render_template("game.html", question=past[len(past) - 1]["question"], runnerup=(past[len(past) - 2]["question"]
               if len(past) > 1 else ""), past=(past[:len(past) - 2][::-1] if len(past) > 2 else ""))
    else:
        return redirect("/game")