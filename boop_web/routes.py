from boop import app, db
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, session
from boop.forms import *
from boop.models import *

@app.route("/", methods=["GET", "POST"])
def welcome():
    
