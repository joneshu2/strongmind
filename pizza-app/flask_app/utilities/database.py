"""
Author: Hunter Jones
"""

import os
import psycopg2
import cryptography
import bcrypt
import json


def get_connection():
  """
  Get and return a connection to the database
  """
  try:
    """
    unix_socket = '/cloudsql/{}'.format("<database_instance_id>")
    conn = psycopg2.connect(
      host=unix_socket, 
      database="strongmind", 
      user="postgres", 
      password="<password>"
      )
    """
    conn = psycopg2.connect(host="host.docker.internal", database="strongmind", port="5432", user="postgres", password="password")
  except Exception as e:
    print("Exception Encountered: ", e)
  else:
    # Return Conneciton object if successfull
    return conn
  # Default return none
  return None

def close_connection(conn):
  """
  Close connection object
  """
  conn.close()

def commit_connection(conn):
  """
  Commit Changes and close connection
  """
  try:
    conn.commit()
  except Exception as e:
    print("Exception Encoutnered: ", e)
    conn.rollback()

def authenticateUser(username, password):
  """
  Authenticate a user login
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##
  
  query = """SELECT users.username, users.password, users.role FROM users WHERE users.username=%s;"""
  cur.execute(query, (username,))
  query_result = cur.fetchall()

  ## Housekeeping
  # Close cursor
  cur.close()
  # Close connection
  close_connection(conn)
  ##

  if query_result:
    user_row = query_result[0]
    # Password returned in index 1 of list
    if password == user_row[1]:
      return {'success': 1, 'username': user_row[0], 'role': user_row[2]}

  return {'failure':0, 'message': "UserNotAuthenticated"}


def getAllToppings():
  """
  Get all toppings in the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  query = """SELECT toppings.id, toppings.name FROM toppings;"""
  cur.execute(query)
  query_result = cur.fetchall()

  ## Housekeeping
  # Close cursor
  cur.close()
  # Close connection
  close_connection(conn)
  ##

  toppings_dict = dict()

  if query_result:
    for row in query_result:
      toppings_dict[row[0]] = {'topping_id': row[0], 'topping_name': row[1]}
  
  return toppings_dict


def createTopping(topping_name):
  """
  Add a topping to the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  check_query = """SELECT * FROM toppings WHERE toppings.name=%s;"""
  cur.execute(check_query, (topping_name,))
  check_query_result = cur.fetchall()

  if check_query_result:
    cur.close()
    close_connection(conn)
    return {'failure': 0, 'message': "ToppingExists"}
  
  query = """INSERT INTO toppings(name) VALUES(%s);"""
  cur.execute(query, (topping_name,))

  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "ToppingAdded"}


def deleteTopping(topping_id):
  """
  Delete a topping from the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  # Delete references to this topping from pizza association table
  delete_reference_query = """DELETE FROM pizzas_toppings where topping_id=%s;"""
  cur.execute(delete_reference_query, (topping_id,))

  delete_query = """DELETE FROM toppings WHERE toppings.id=%s;"""
  cur.execute(delete_query, (topping_id,))
  
  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "ToppingDeleted"}


def getAllPizzas():
  """
  Get all pizzas in the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  query = """SELECT pizzas.id, pizzas.name FROM pizzas;"""
  cur.execute(query)
  query_result = cur.fetchall()

  ## Housekeeping
  # Close cursor
  cur.close()
  # Close connection
  close_connection(conn)
  ##

  pizzas_dict = dict()

  if query_result:
    for row in query_result:
      pizzas_dict[row[0]] = {'pizza_id': row[0], 'pizza_name': row[1]}
  
  return pizzas_dict


def createPizza(pizza_name):
  """
  Add a pizza to the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  check_query = """SELECT * FROM pizzas WHERE pizzas.name=%s;"""
  cur.execute(check_query, (pizza_name,))
  check_query_result = cur.fetchall()

  if check_query_result:
    cur.close()
    close_connection(conn)
    return {'failure': 0, 'message': "PizzaExists"}
  
  query = """INSERT INTO pizzas(name) VALUES(%s);"""
  cur.execute(query, (pizza_name,))

  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "PizzaAdded"}


def deletePizza(pizza_id):
  """
  Delete a pizza from the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  # Delete references to this pizza from pizza topping association table
  delete_reference_query = """DELETE FROM pizzas_toppings where pizza_id=%s;"""
  cur.execute(delete_reference_query, (pizza_id,))

  delete_query = """DELETE FROM pizzas WHERE pizzas.id=%s;"""
  cur.execute(delete_query, (pizza_id,))
  
  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "PizzaDeleted"}


def getPizzaToppings(pizza_id):
  """
  Get all toppings related to the pizza
  """

  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  query = """SELECT toppings.id, toppings.name FROM pizzas_toppings JOIN toppings ON pizzas_toppings.topping_id = toppings.id WHERE pizzas_toppings.pizza_id=%s;"""
  cur.execute(query, (pizza_id,))
  query_result = cur.fetchall()

  ## Housekeeping
  # Close cursor
  cur.close()
  # Close connection
  close_connection(conn)
  ##

  pizza_toppings_dict = dict()

  if query_result:
    for row in query_result:
      pizza_toppings_dict[row[0]] = {'topping_id': row[0], 'topping_name': row[1]}
  
  return pizza_toppings_dict


def removeTopping(topping_id, pizza_id):
  """
  Remove a topping from a pizza in the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  # Delete references to this topping from pizza association table with matching pizza id
  remove_reference_query = """DELETE FROM pizzas_toppings where topping_id=%s AND pizza_id=%s;"""
  cur.execute(remove_reference_query, (topping_id, pizza_id))
  
  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "ToppingRemoved"}


def addTopping(topping_id, pizza_id):
  """
  Add a topping to a pizza in the database
  """
  ## Housekeeping
  # Get connection 
  conn = get_connection()
  if not conn:
    return {'failure':0, 'message': "DatabaseConnectionFailed"}
  # Get cursor
  cur = conn.cursor()
  ##

  # Check if there is already an association
  reference_check_query = """SELECT * FROM pizzas_toppings where topping_id=%s AND pizza_id=%s;"""
  cur.execute(reference_check_query, (topping_id, pizza_id))
  
  query_result = cur.fetchall()
  if query_result:
    cur.close()
    close_connection(conn)
    return {'failure': 0, 'message': 'ToppingAlreadyAdded'}

  # Add references to this topping from pizza association table with matching pizza id
  add_reference_query = """INSERT INTO pizzas_toppings(pizza_id, topping_id) VALUES(%s,%s);"""
  cur.execute(add_reference_query, (pizza_id, topping_id))
  
  ## Housekeeping
  # Close cursor
  cur.close()
  # Commit connection
  commit_connection(conn)
  # Close connection
  close_connection(conn)
  ##
  return {'success': 1, 'message': "ToppingAdded"}