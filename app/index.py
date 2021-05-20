from flask.globals import request
from flask.templating import render_template
from app import app

@app.route("/")
def home():
    if request.cookies.get("user-token"):
        return render_template("dashboard.html")
    else:
        return render_template("index.html")
