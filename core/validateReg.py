from app import app, request, make_response
from src.reg_core import addUser
import hashlib


@app.route("/api/validate/users/registration" ,methods=["POST"])
def validateReg():
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            uname = request.form["uname"]
            pwd = request.form["pwd"]
            email = request.form["email"]
            credentials = {
                "fname": fname,
                "uname": uname,
                "pwd": pwd,
                "email": email,
            }
            userToken = hashlib.md5((uname+pwd).encode())
            resp = make_response(addUser(credentials))
            
            resp.set_cookie("user-token", userToken.hexdigest())
        
            return resp, 200
        except:
            return "Bad Request as well", 400

