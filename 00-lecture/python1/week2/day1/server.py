from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
  list_of_stuff = ["thing", "other thing", "third thing"]
  return render_template('index.html', stuff=list_of_stuff)

@app.route('/process', methods=["POST"])
def process():
  # do some stuff
  print(request.form['first-name'], request.form['last-name'])
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)