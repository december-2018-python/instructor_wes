from .mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = 'ninja_gold_december'

def validate(form_data):
  errors = []
  if len(form_data['first_name']) < 2:
    errors.append('First name must be at least 2 characters long')
  if len(form_data['last_name']) < 2:
    errors.append("Last name must be at least 2 characters long")
  if len(form_data['password']) < 8:
    errors.append("Password must be at least 8 characters long")
  if form_data['password'] != form_data['confirm']:
    errors.append("Passwords don't match")
  if not EMAIL_REGEX.match(form_data['email']):
    errors.append("Email must be valid")

  return errors

def create(form_data, bcrypt):
  # hash user's password
  pw_hash = bcrypt.generate_password_hash(form_data['password'])
  # create user
  db = connectToMySQL(SCHEMA)
  query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW());'
  data = {
    'first_name': form_data['first_name'],
    'last_name': form_data['last_name'],
    'email': form_data['email'],
    'pw_hash': pw_hash,
  }
  user_id = db.query_db(query, data)
  return user_id

def check_login(form_data, bcrypt):
  errors = []

  db = connectToMySQL(SCHEMA)
  query = 'SELECT email, pw_hash, id FROM users WHERE email = %(email)s;'
  data = {
    "email": form_data['email']
  }
  user_list = db.query_db(query, data)
  if not user_list:
    errors.append("Email or password incorrect")
  else:
    user = user_list[0]
    if bcrypt.check_password_hash(user['pw_hash'], form_data['password']):
      # user is good, log them in
      return (True, user['id'])
    else:
      errors.append("Email or password incorrect")

  return (False, errors)

def get_current(user_id):
  db = connectToMySQL(SCHEMA)
  query = 'SELECT * FROM users WHERE id = %(user_id)s;'
  data = {
    "user_id": user_id
  }
  # user_list = db.query_db(query, data)
  # user = user_list[0]
  # return user
  return db.query_db(query, data)[0]