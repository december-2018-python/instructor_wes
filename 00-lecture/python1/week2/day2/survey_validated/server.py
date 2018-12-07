from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "asdfkjslkajf;lkwjefpoiasdfj"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  errors = False

  if len(request.form['first_name']) == 0:
    flash('First name cannot be blank')
    errors = True
  
  if len(request.form['last_name']) == 0:
    flash('Last name cannot be blank')
    errors = True

  if len(request.form['email']) < 5:
    flash("Email must be valid")
    errors = True

  if errors:
    return redirect('/')
  else:
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['favorite_language'] = request.form['favorite_language']
    session['location'] = request.form['location']
    return redirect('/success')

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/colors/<color>')
def colors(color):
  print(color)
  return render_template('color.html', col=color)

if __name__ == "__main__":
  app.run(debug=True)