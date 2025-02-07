"""
Author: Hunter Jones
"""

from flask import current_app as app
from flask import render_template, redirect, request, session, url_for, jsonify, copy_current_request_context
from werkzeug.datastructures import ImmutableMultiDict
import json
import functools


@app.route('/')
def root():
  """
  Index route return to a home splash page
  """
  return redirect('/home')

@app.route('/home')
def home():
  """
  Home page to be initially used as splash page
  """
  return render_template('home.html')


################
# Utility/Miscellaneous Routes
################

@app.route("/static/<path:path>")
def static_dir(path):
  return send_from_directory("static", path)

@app.after_request
def add_header(res):
  res.headers["Cache-Control"] = "no-cache, no-store, public, max-age=0, must-revalidate"
  res.headers["Pragma"] = "no-cache"
  res.headers["Expires"] = "0"
  return res