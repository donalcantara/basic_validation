from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
	if len(request.form['comment']) < 2:
		flash("Comments cannot be empty!")
	return redirect('/')
	session['name'] = request.form['name']
	session['comment'] = request.form['comment']
	session['language'] = request.form['language']
	session['location'] = request.form['location']
	return render_template('result.html')

@app.route('/goback', methods=['POST'])
def goback():
  return render_template('index.html')

app.run(debug=True)