from flask import Flask, session, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from helpers import users, locations, activities

SCHEMA = 'ninja_gold_december'

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"

app = Flask(__name__)
app.secret_key = 'as;ldkfjasdl;fashldkfwjkefawe'

@app.route('/')
def index():
  if 'user_id' not in session:
    return redirect('/users/new')

  return render_template('index.html',
    user = users.get_current(session['user_id']),
    locations = locations.get_all(),
    activities = activities.get_all_for_current_user(session['user_id'])
  )

@app.route('/users/new')
def new_user():
  return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create():
  errors = users.validate(request.form)
  if errors:
    for error in errors:
      flash(error)
    return redirect('/users/new')
  
  user_id = users.create(request.form, bcrypt)
  session['user_id'] = user_id
  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  valid, response = users.check_login(request.form, bcrypt)
  if valid:
    session['user_id'] = response
    return redirect('/')
  else:
    for error in response:
      flash(error)
    return redirect('/users/new')

if __name__ == "__main__":
  app.run(debug=True)