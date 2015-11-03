# part 1

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(list):
	for i in list:
		line = ''
		for j in range(i):
			line += '*'
		print line

draw_stars(x)
print

# part 2

y = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']

def draw_stars_2(list):
	for i in list:
		line = ''
		n = 0
		if type(i) == str:
			iter_char = i[:1].lower()
			n = len(i)
		elif type(i) == int:
			iter_char = '*'
			n = i
		for j in range(n):
			line += iter_char
		print line

draw_stars_2(y)


