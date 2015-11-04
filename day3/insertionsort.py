import random, datetime

def new_sample_list():
	new_list = []
	for i in range(100):
		new_list.append(int(round(random.random() * 10000)))
	return new_list

arr = [6, 5, 3, 1, 8, 7, 2, 4]

def insertion_sort(list):
	start = datetime.datetime.now()
	for i in range(1, len(list)):
		val = list[i]
		valIndex = i
		while valIndex > 0 and list[valIndex - 1] > val:
			list[valIndex] = list[valIndex - 1]
			valIndex = valIndex - 1
		list[valIndex] = val
	end = datetime.datetime.now()
	print 'it took ' + str(end - start) + ' to complete'
	return list

#print insertion_sort(arr)
print insertion_sort(new_sample_list())













