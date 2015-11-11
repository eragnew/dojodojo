from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'wow, such secret, much awesome'
mysql = MySQLConnector('friendsdb')

@app.route('/')
def index():
	query = 'SELECT * FROM friends'
	friends = mysql.fetch(query)
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	if (len(request.form['first_name']) < 1) or (len(request.form['last_name']) < 1) or (len(request.form['occupation']) < 1):
		flash('All fields are required!')
		return redirect('/')
	query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ("%s", "%s", "%s", NOW(), NOW())' % (request.form['first_name'], request.form['last_name'], request.form['occupation'])
	mysql.run_mysql_query(query)
	flash('New friend added!')
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = 'SELECT * FROM friends WHERE id=%s' % id
	friend = mysql.fetch(query)
	return render_template('edit_friend.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	if (len(request.form['first_name']) < 1) or (len(request.form['last_name']) < 1) or (len(request.form['occupation']) < 1):
		flash('All fields are required!')
		return redirect('/friends/' + id + '/edit')
	query = 'UPDATE friends SET first_name="%s", last_name="%s", occupation="%s", updated_at=NOW() WHERE id=%s' % (request.form['first_name'], request.form['last_name'], request.form['occupation'], id)
	mysql.run_mysql_query(query)
	flash('Changes saved!')
	return redirect('/friends/' + id + '/edit')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = 'DELETE FROM friends WHERE id=%s' % id
	mysql.run_mysql_query(query)
	flash('Friend removed from the database!')
	return redirect('/')

app.run(debug=True)









