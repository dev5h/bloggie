from app import app, render_template, redirect, request
@app.route("/interests")
def interest():
    with open("db/interests.txt", "r") as f:
        raw = f.read()
        interest_list = raw.split(",")
        f.close()
    if request.cookies.get("user-token"):
        return render_template("interest.html", list= interest_list)
        
    else:
        return redirect("/login")