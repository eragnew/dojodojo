a = [1, 2, 5, 10, 255, 3]

def avg(list):
	total = 0
	for i in list:
		total += i
	return total / len(list)

print avg(a)