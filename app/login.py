
from app import app, request, redirect, render_template
@app.route("/login", methods=["GET"])
def login():
    if request.cookies.get("user-token"):
        return redirect("/")
    else:
        return render_template("login.html")