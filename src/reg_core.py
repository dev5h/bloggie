import sqlite3
import hashlib
from validate_email import validate_email


def registerToDB(credentials):
    fname = credentials["fname"]
    uname = credentials["uname"]
    pwd = credentials["pwd"]
    hashedPwd = hashlib.md5(pwd.encode())
    email = credentials["email"]
    userToken = hashlib.md5((uname+pwd).encode('utf-8'))
    con = sqlite3.connect('db/users.db')
    curs = con.cursor()
    SQL = "INSERT INTO users ('fname', 'uname', 'pwd', 'email', 'token') VALUES (?,?, ?, ?, ?)"
    curs.execute(SQL, (fname, uname, hashedPwd.hexdigest(), email, userToken.hexdigest()))
    con.commit()
    con.close()

def addUser(credentials):
    STATUS = 200
    fname = credentials["fname"]
    uname = credentials["uname"]
    pwd = credentials["pwd"]
    email = credentials["email"]

    if len(fname)>0 and len(uname) > 0 and len(pwd) > 0 and len(email) >0:
        STATUS = 200
        if len(fname) < 6:
            STATUS = "shrtfname"
        elif len(uname) < 4:
            STATUS = "shrtuname"
        elif len(pwd) < 6:
            STATUS = "shrtpwd"
        elif validate_email(email) == False:
            STATUS = "invalidEmail"
        else:
            STATUS = 200

    else:
        STATUS = "nullValue"
    
    if STATUS == 200:
        registerToDB(credentials)
        return "success", 200
    else:
        return "failed", 201




