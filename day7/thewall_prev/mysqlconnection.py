import mysql.connector
import collections

def _convert(data):
	if isinstance(data, basestring):
		return str(data)
	elif isinstance(data, collections.Mapping):
		return dict(map(_convert, data.iteritems()))
	elif isinstance(data, collections.Iterable):
		return type(data)(map(_convert, data))
	else:
		return data

class MySQLConnection(object):
	def __init__(self, db):
		self.config = {
			'user': 'root',
#			'password': 'root',
			'database': db,
			'host': 'localhost',
			'unix_socket': '/tmp/mysql.sock'
		}
		self.conn = mysql.connector.connect(**self.config)
	def fetch(self, query):
		cursor = self.conn.cursor(dictionary=True)
		cursor.execute(query)
		data = list(cursor.fetchall())
		cursor.close()
		return _convert(data)
	def run_mysql_query(self, query):
		cursor = self.conn.cursor(dictionary=True)
		data = cursor.execute(query)
		self.conn.commit()
		cursor.close()
		return data

def MySQLConnector(db):
	return MySQLConnection(db)



