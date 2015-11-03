print 'Scores and Grades'

for i in range(10):
	score = int(raw_input('Enter score: '))
	if score >= 60 and score < 70:
		grade = 'D'
	elif score >= 70 and score < 80:
		grade = 'C'
	elif score >= 80 and score < 90:
		grade = 'B'
	elif score >= 90 and score <= 100:
		grade = 'A'
	else:
		grade = 'undefined :('
	print 'Score: %s; Your grade is %s' % (score, grade)

print 'End of the program. Bye!'