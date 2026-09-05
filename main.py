from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])
def create():
    return render_template("create.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=False)
