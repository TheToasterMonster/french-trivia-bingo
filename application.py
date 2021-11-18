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
    # get a new questions list and clear past history
    qs = qbank.copy()
    past.clear()
    return


@app.route("/", methods=["GET", "POST"])
def index():
    """Show button to start a game"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        # reset game first before starting another
        cleargame()
        return redirect("/game")


@app.route("/game", methods=["GET", "POST"])
def game():
    """starts displaying bingo questions"""
    if request.method == "GET":
        # send user back to main menu if out of questions
        if len(qs) == 0:
            return redirect("/")
        # get a random question from the list
        past.append(qs.pop(random.randint(0, len(qs) - 1)))
        # feed current question, last question, and past questions into the html file
        return render_template("game.html", question=past[len(past) - 1]["question"], runnerup=(past[len(past) - 2]["question"]
               if len(past) > 1 else ""), past=(past[:len(past) - 2][::-1] if len(past) > 2 else []))
    else:
        return redirect("/game")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    """generates bingo boards"""
    if request.method == "GET":
        return render_template("generate.html")
    else:
        # get number of boards from the user
        amount = int(request.form.get("amount"))
        # initiate blank boards
        boards = [[] for i in range(amount)]
        for i in range(amount):
            # get a fresh question bank for each board
            bank = qbank.copy()
            # place an answer in each box in 5x5 grid, with middle being "FREE"
            for j in range(5):
                boards[i].append([])
                for k in range(5):
                    if j == 2 and k == 2:
                        boards[i][j].append("FREE")
                    else:
                        boards[i][j].append(bank.pop(random.randint(0, len(bank) - 1))["answer"])
        return render_template("boards.html", boards=boards)
