import re
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

app = Flask(__name__)
app.secret_key = 'wow, so secret, much wow'

mysql = MySQLConnector('emaildb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def create():
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Email is not a valid email address!')
		return redirect('/')
	else:
		query = 'INSERT INTO email (email, created_at) VALUES ("%s", NOW())' % (request.form['email'], )
		print query
		mysql.run_mysql_query(query)
		query = 'SELECT * FROM email'
		emails = mysql.fetch(query)
		return render_template('success.html', new_email=request.form['email'], emails=emails)

@app.route('/delete', methods=['POST'])
def delete():
	query = 'DELETE FROM email WHERE id=%s' % request.form['id']
	print query
	mysql.run_mysql_query(query)
	query = 'SELECT * FROM email'
	emails = mysql.fetch(query)
	return render_template('success.html', new_email=None, emails=emails)

app.run(debug=True)





