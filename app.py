from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "freegame123"

@app.route("/", methods=["GET", "POST"])
def game():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["message"] = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        number = session["number"]

        if guess < number:
            session["message"] = "Too Low ❌"
        elif guess > number:
            session["message"] = "Too High ❌"
        else:
            session["message"] = "🎉 Correct! You Win!"
            session.pop("number")

    return render_template("index.html", message=session["message"])

if __name__ == "__main__":
    app.run()
