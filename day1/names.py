users = {
	'Students': [
		{'first_name': 'Michael', 'last_name': 'Jordan'},
		{'first_name': 'John', 'last_name': 'Rosales'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'}
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'Martin', 'last_name': 'Puryear'}
	]
}

print 'Students'

students = users['Students']

for i in range(len(students)):
	name = students[i]['first_name'].upper() + ' ' + students[i]['last_name'].upper()
	print '%d - %s - %d' % (i + 1, name, len(name) - 1)

print 'Instructors'

instructors = users['Instructors']

for i in range(len(instructors)):
	name = instructors[i]['first_name'].upper() + ' ' + instructors[i]['last_name'].upper()
	print '%d - %s - %d' % (i + 1, name, len(name) - 1)

