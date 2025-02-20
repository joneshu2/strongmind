"""
Author: Hunter Jones
"""

from flask import current_app as app
from flask import render_template, redirect, request, session, url_for, jsonify, copy_current_request_context
from werkzeug.datastructures import ImmutableMultiDict
import json
import functools
from .utilities.database import *


########################
# AUTH Protected Routes
########################
def login_required(func):
  @functools.wraps(func)
  def secure_function(*args, **kwargs):
    if "username" not in session:
      return redirect(url_for("login"))


def getUserName():
  """
  Get username stored in the user's session or 'Unknown' if no username value in the session
  """
  return session['username'] if 'username' in session else 'Unknown'

def getUserRole():
  """
  Get user role stored in the user's session or default to 'guest' if no userrole value in the session
  """
  return session['userrole'] if 'userrole' in session else 'guest'

@app.route('/')
def root():
  """
  Route return to a home splash page
  """
  return redirect('/home')

@app.route('/home')
def home():
  """
  Home page to be initially used as splash page
  """
  return render_template('home.html', user_name=getUserName(), user_role=getUserRole())

@app.route('/login')
def login():
  """
  Login page route to accept credentials for a login attempt
  """
  return render_template('login.html', user_name=getUserName(), user_role=getUserRole())

@app.route('/logout')
def logout():
  """
  Logout function removes username and userrole from session
  """
  session.pop('username', default=None)
  session.pop('userrole', default=None)
  return redirect('/home')

@app.route('/authenticatelogin', methods=["POST", "GET"])
def authenticatelogin():
  """
  Logic of processing authenticating credentials and if validated adds username variable and userrole to user session
  """
  # Get form fields submitted
  form_fields = dict((key, request.form.getlist(key)[0]) for key in list(request.form.keys()))
  # Collect username and password fields to process
  username_field = form_fields['username']
  password_field = form_fields['password']

  # Store result of authentication
  auth_status = authenticateUser(username_field, password_field)

  # If authentication success then add username and userrole variables to user session
  if 'success' in auth_status:
    session['username'] = auth_status['username']
    session['userrole'] = auth_status['role']

  return json.dumps(auth_status)


################
# Owner Related
################

@login_required
@app.route('/manage-toppings', methods=["POST", "GET"])
def managetoppings():
  """
  Manage Toppings page to be used by the owner
  """
  toppings = getAllToppings()
  return render_template('manage-toppings.html', user_name=getUserName(), user_role=getUserRole(), current_toppings=toppings)

@app.route('/processtoppingcreation', methods = ["POST"])
def processtoppingcreation():
  """
  Logic processing of topping creation
  """
  # Collect form fields
  topping_form = request.form
  name_field = topping_form.get('topping-name-input')

  # Attempt to add topping
  topping_creation_status = createTopping(topping_name=name_field)
  print(topping_creation_status)

  # Redirect to toppings management page
  return redirect('/manage-toppings')

@app.route('/processtoppingdeletion', methods = ["POST"])
def processtoppingdeletion():
  """
  Logic of processing topping deletion
  """
  # Get fields submitted
  form_fields = dict((key, request.form.getlist(key)[0]) for key in list(request.form.keys()))
  topping_id_field = form_fields['topping_id']

  # Attempt to delete topping
  topping_deletion_status = deleteTopping(topping_id=topping_id_field)
  print(topping_deletion_status)

  return json.dumps(topping_deletion_status)

################
# Chef Related
################

@login_required
@app.route('/manage-pizzas')
def managepizzas():
  """
  Manage Pizzas page to be used by a chef
  """
  pizzas = getAllPizzas()
  return render_template('manage-pizzas.html', user_name=getUserName(), user_role=getUserRole(), current_pizzas=pizzas)

@app.route('/processpizzacreation', methods = ["POST"])
def processpizzacreation():
  """
  Logic processing of pizza creation
  """
  # Collect form fields
  pizza_form = request.form
  name_field = pizza_form.get('pizza-name-input')

  # Attempt to add pizza
  pizza_creation_status = createPizza(pizza_name=name_field)
  print(pizza_creation_status)

  # Redirect to pizzas management page
  return redirect('/manage-pizzas')


@app.route('/processpizzadeletion', methods = ["POST"])
def processpizzadeletion():
  """
  Logic of processing pizza deletion
  """
  # Get fields submitted
  form_fields = dict((key, request.form.getlist(key)[0]) for key in list(request.form.keys()))
  pizza_id_field = form_fields['pizza_id']

  # Attempt to delete pizza
  pizza_deletion_status = deletePizza(pizza_id=pizza_id_field)
  print(pizza_deletion_status)

  return json.dumps(pizza_deletion_status)

@login_required
@app.route('/manage-pizzas/<int:pizza_id>')
def pizza(pizza_id):
  """
  Route for a specific pizza identified by its primary key pizza_id
  """
  # Geth the dictionary of current pizza information
  current_pizza_toppings = getPizzaToppings(pizza_id)
  all_toppings = getAllToppings()
  return render_template('pizza.html', user_name=getUserName(), user_role=getUserRole(), current_pizza_id=pizza_id, current_toppings=current_pizza_toppings, available_toppings=all_toppings)

@app.route('/processremovetopping', methods = ["POST"])
def processremovetopping():
  """
  Logic of processing topping removal from a pizza
  """
  # Get fields submitted 
  form_fields = dict((key, request.form.getlist(key)[0]) for key in list(request.form.keys()))
  topping_id_field = form_fields['topping_id']
  pizza_id_field = form_fields['pizza_id']

  # Attempt to delete topping
  topping_removal_status = removeTopping(topping_id=topping_id_field, pizza_id=pizza_id_field)

  return json.dumps(topping_removal_status)


@app.route('/processaddtopping', methods = ["POST"])
def processaddtopping():
  """
  Logic of processing adding a topping to a pizza
  """
  # Get fields submitted 
  form_fields = dict((key, request.form.getlist(key)[0]) for key in list(request.form.keys()))
  topping_id_field = form_fields['topping_id']
  pizza_id_field = form_fields['pizza_id']

  print(topping_id_field, pizza_id_field)

  # Attempt to add a topping
  topping_addition_status = addTopping(topping_id=topping_id_field, pizza_id=pizza_id_field)

  return json.dumps(topping_addition_status)
  

################
# Utility/Miscellaneous Routes
################

@app.route("/static/<path:path>")
def static_dir(path):
  return send_from_directory("static", path)

@app.after_request
def add_header(response):
  response.headers["Cache-Control"] = "no-cache, no-store, public, max-age=0, must-revalidate"
  response.headers["Pragma"] = "no-cache"
  response.headers["Expires"] = "0"
  return response