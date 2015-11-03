a = [2, 4, 10, 16]

def multiply(list, factor):
	new_list = []
	for i in list:
		new_list.append(i * factor)
	return new_list

print multiply(a, 5)