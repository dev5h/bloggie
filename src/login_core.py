import sqlite3
import hashlib


def isLoginValid(crd):
    con = sqlite3.connect("db/users.db")
    uname = crd["uname"]
    pwd = crd["pwd"]
    userToken = hashlib.md5((uname+pwd).encode('utf-8'))
    curs = con.cursor()
    curs.execute(f"SELECT * FROM users WHERE token = '{userToken.hexdigest()}' ")
    row = curs.fetchall()
    con.close()
    if len(row) == 1:
        return True
    else:
        return False

