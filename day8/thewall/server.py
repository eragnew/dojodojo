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
	session['user'] = {
		'user_id': user[0]['user_id'],
		'first_name': user[0]['first_name']
	}
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
	session['user'] = {
		'user_id': user[0]['user_id'],
		'first_name': user[0]['first_name']
	}
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
#	query = 'SELECT * FROM messages ORDER BY created_at DESC'
	query = '''
	SELECT a.message_id, b.first_name, b.last_name, a.message,
		DATE_FORMAT(a.created_at, "%m/%d/%Y %h:%i %p") AS created_at
	FROM messages AS a
	INNER JOIN users AS b ON a.user_id = b.user_id
	ORDER BY a.created_at DESC
	'''
	messages = mysql.fetch(query)
	for message in messages:
		query = 'SELECT a.comment_id, b.first_name, b.last_name, a.comment, DATE_FORMAT(a.created_at, "%m/%d/%Y %h:%i %p") AS created_at FROM comments AS a INNER JOIN users AS b ON a.user_id = b.user_id WHERE a.message_id = {} ORDER BY a.created_at'.format(str(message['message_id']))
		comments = mysql.fetch(query)
		message['comments'] = comments
	return render_template('wall.html', messages=messages)

@app.route('/messages', methods=['POST'])
def create_message():
	if len(request.form['message']) < 1:
		flash('Message cannot be empty.')
		return redirect('/wall')
	query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (%s, "%s", NOW(), NOW())' % (str(request.form['user_id']), str(request.form['message']))
	mysql.run_mysql_query(query)
	flash('New message posted.')
	return redirect('/wall')

@app.route('/messages/<id>/delete', methods=['POST'])
def delete_message(id):
	query = 'DELETE FROM comments WHERE message_id=%s' % str(id)
	mysql.run_mysql_query(query)
	query = 'DELETE FROM messages WHERE message_id=%s' % str(id)
	mysql.run_mysql_query(query)
	flash('Message deleted.')
	return redirect('/wall')

@app.route('/comments', methods=['POST'])
def create_comment():
	if len(request.form['comment']) < 1:
		flash('Comment cannot be empty.')
		return redirect('/wall')
	query = 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (%s, %s, "%s", NOW(), NOW())' % (str(request.form['message_id']), str(request.form['user_id']), str(request.form['comment']))
	mysql.run_mysql_query(query)
	flash('New comment posted.')
	return redirect('/wall')

app.run(debug=True)






