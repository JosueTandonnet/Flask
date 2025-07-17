from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.join("flaskr", "templates"))

@app.route("/")
def home():
    return render_template("blog/index.html")
