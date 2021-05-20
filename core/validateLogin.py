from app import app, request, make_response
from src.login_core import isLoginValid
import hashlib
@app.route("/api/validate/users/login", methods=["POST"])
def validateLogin():
    if request.method == "POST":
        try:
            uname = request.form["uname"]
            pwd = request.form["pwd"]
            userToken = hashlib.md5((uname+pwd).encode())
            credentials = {
                "uname": uname,
                "pwd": pwd,
            }

            isValidLogin = isLoginValid(credentials)
            if isValidLogin:
                resp = make_response("success")
                resp.set_cookie("user-token", userToken.hexdigest())
                return resp, 200
            else:
                return "wrongcrd", 400
            
        except Exception as e:
            return str(e), 500
            

