from flask import Flask
from flask import Flask, redirect, render_template, request, make_response


app = Flask(__name__, template_folder="../templates", static_folder="../static")


from app import index
from app import join
from app import login
from core import validateReg
from core import validateLogin
from app import interests