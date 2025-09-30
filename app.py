from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/Identify")
def Identify():
    return render_template("identify.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)