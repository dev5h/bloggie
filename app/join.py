from app import app, request, render_template, redirect

@app.route("/join")
def join():
    if "user-token" in request.cookies:
        return redirect("/")
    else:
        return render_template("join.html")
