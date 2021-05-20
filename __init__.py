from flask import Flask, render_template, request, make_response , redirect, url_for
import src
import hashlib

app = Flask(__name__)
from app import ro