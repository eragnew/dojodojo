import re
import bcrypt
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

app = Flask(__name__)
app.secret_key = 'wow, such secret, much awesome'

mysql = MySQLConnector('thewalldb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	if len(request.form['first_name']) < 2 or (not request.form['first_name'].isalpha()):
		flash('First Name must have at least 2 characters and cannot contain any numbers.')
		return redirect('/')
	elif len(request.form['last_name']) < 2 or (not request.form['last_name'].isalpha()):
		flash('Last Name must have at least 2 characters and cannot contain any numbers.')
		return redirect('/')
	elif len(request.form['email']) < 1 or (not EMAIL_REGEX.match(request.form['email'])):
		flash('Please enter a valid email address.')
		return redirect('/')
	elif len(request.form['password']) < 8:
		flash('Password must contain at least 8 characters.')
		return redirect('/')
	elif request.form['password'] != request.form['confirm_password']:
		flash('Passwords do not match!')
		return redirect('/')
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(str(request.form['password']), salt)
	query = 'INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES ("%s", "%s", "%s", "%s", "%s", NOW(), NOW())' % (request.form['first_name'], request.form['last_name'], request.form['email'], hashed_password, salt)
	mysql.run_mysql_query(query)
	query = 'SELECT * FROM users WHERE email="%s"' % request.form['email']
	user = mysql.fetch(query)
	session['user'] = user[0]
	return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
	if len(request.form['email']) < 1:
		flash('Email cannot be blank.')
		return redirect('/')
	elif len(request.form['password']) < 1:
		flash('Password cannot be blank.')
		return redirect('/')
	query = 'SELECT * FROM users WHERE email="%s"' % request.form['email']
	user = mysql.fetch(query)
	if len(user) < 1:
		flash('Email not found. Please check or register as new user.')
		return redirect('/')
	if bcrypt.hashpw(str(request.form['password']), user[0]['salt']) != user[0]['password']:
		flash('Login error. Please try again.')
		return redirect('/')
	session['user'] = user[0]
	return redirect('/wall')

@app.route('/logout')
def logout():
	session.clear()
	flash('You were logged out.')
	return redirect('/')

@app.route('/wall')
def wall():
	if not session.get('user'):
		flash('Please log in.')
		return redirect('/')
	return render_template('wall.html')

@app.route('/messages', methods=['POST'])
def create_message():
	pass

@app.route('/messages/<id>/delete', methods=['POST'])
def delete_message(id):
	pass

@app.route('/comments', methods=['POST'])
def create_comment():
	pass

app.run(debug=True)






