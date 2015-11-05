import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'this is a secret'

@app.route('/')
def index():
	session['number'] = random.randrange(0, 101)
	print 'setting number to %d...' % session['number']
  	return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
	guess = int(request.form['number'])
	if guess > session['number']:
		return 'too high'
	elif guess < session['number']:
		return 'too low'
	elif guess == session['number']:
		session.pop('number')
		return 'got it'

app.run(debug=True)
