from flask import Flask
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector('mydb')

print mysql.fetch('SELECT * FROM users')

app.run(debug=True)