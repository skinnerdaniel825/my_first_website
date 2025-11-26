from flask import Flask, render_template, request
import os

app = Flask(__name__)

END_STATE = "end.flag"

def solved():
    return os.path.exists(END_STATE)

@app.route("/")
def display_to_user():
    if solved():
        return render_template("end.html")
    else:
        return render_template("index.html")
    
@app.route("/check_password", methods=["POST"])
def check_password():
    password = request.form.get("password")
# why are there no curly braces in python? This sucks.

    if password == "password":
        return render_template("authorized.html")
    else:
        return render_template("index.html", error="Incorrect password.")

@app.route("/unlock", methods=["POST"])
def unlock():
    with open(END_STATE, "w") as endFile:
        endFile.write("true")
    return render_template("end.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)