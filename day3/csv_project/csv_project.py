import csv

# THIS GIVES ME AN ERROR :(
#with open('us-500.csv', 'rb') as f:
#	reader = csv.reader(f)
#	for row in reader:
#		print row

# rolling my own
f = open('us-500.csv', 'rb')

file_data = f.read()
data = file_data.split('\r')[1:]

for line in data:
	line_data = line.split(',')
	if len(line_data) == 12:
		first_name = line_data[0][1:-1]
		last_name = line_data[1][1:-1]
		company_name = line_data[2][1:-1]
		address = line_data[3][1:-1]
		city = line_data[4][1:-1]
		county = line_data[5][1:-1]
		state = line_data[6][1:-1]
		zip = line_data[7]
		phone1 = line_data[8][1:-1]
		phone2 = line_data[9][1:-1]
		email = line_data[10][1:-1]
		web = line_data[11][1:-1]
	elif len(line_data) == 13:
		first_name = line_data[0][1:-1]
		last_name = line_data[1][1:-1]
		company_name = line_data[2][1:] + line_data[3][:-1]
		address = line_data[4][1:-1]
		city = line_data[5][1:-1]
		county = line_data[6][1:-1]
		state = line_data[7][1:-1]
		zip = line_data[8]
		phone1 = line_data[9][1:-1]
		phone2 = line_data[10][1:-1]
		email = line_data[11][1:-1]
		web = line_data[12][1:-1]
	print first_name + ' ' + last_name
	print 'first_name: ' + first_name
	print 'last_name: ' + last_name
	print 'company_name: ' + company_name
	print 'address: ' + address
	print 'city: ' + city
	print 'county: ' + county
	print 'state: ' + state
	print 'zip: ' + zip
	print 'phone1: ' + phone1
	print 'phone2: ' + phone2
	print 'email: ' + email
	print 'web: ' + web
	print '------------'












