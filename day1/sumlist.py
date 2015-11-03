a = [1, 2, 5, 10, 255, 3]

def sum(list):
	total = 0
	for i in list:
		total += i
	return total

print sum(a)