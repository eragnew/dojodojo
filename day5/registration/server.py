import re
from flask import Flask, render_template, request, redirect, session, flash

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

app = Flask(__name__)
app.secret_key = 'wow, so secret, much wow'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	redirect_back = False
	if len(request.form['first_name']) < 1:
		flash('First Name is required!')
		redirect_back = True
	if len(request.form['last_name']) < 1:
		flash('Last Name is required!')
		redirect_back = True
	if len(request.form['email']) < 1:
		flash('Email is required!')
		redirect_back = True
	if len(request.form['password']) < 1:
		flash('Password is required!')
		redirect_back = True
	if len(request.form['confirm_password']) < 1:
		flash('Confirm Password is required!')
		redirect_back = True
	if not request.form['first_name'].isalpha():
		flash('First Name can only contain letters!')
		redirect_back = True
	if not request.form['last_name'].isalpha():
		flash('Last Name can only contain letters!')
		redirect_back = True
	if len(request.form['password']) < 8:
		flash('Password must be at least 8 characters!')
		redirect_back = True
	if request.form['password'] != request.form['confirm_password']:
		flash('Passwords do not match!')
		redirect_back = True
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Email is not a valid email address!')
		redirect_back = True
	if not any([l for l in request.form['password'] if l.isupper()]):
		flash('Password must contain at least 1 capital letter!')
		redirect_back = True
	if not any([l for l in request.form['password'] if l.isdigit()]):
		flash('Password must contain at least 1 number!')
		redirect_back = True
	if redirect_back:
		return redirect('/')
	else:
		return 'Thank you for registering :)'

app.run(debug=True)



