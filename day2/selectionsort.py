import random, datetime

# selection sort ... my first attempt

#arr = [6, 5, 3, 1, 8, 7, 2, 4]

def new_sample_list():
	new_list = []
	for i in range(100):
		new_list.append(int(round(random.random() * 10000)))
	return new_list

def new_big_sample_list():
	new_list = []
	for i in range(10000):
		new_list.append(int(round(random.random() * 10000)))
	return new_list

def selection_sort(list):
	count = 0
	start = datetime.datetime.now()
	for i in range(len(list)):
		min, minIndex = list[i], i
		for j in range(i, len(list)):
			count += 1
			if list[j] < min:
				min = list[j]
				minIndex = j
		itemToMove = list[minIndex]
		list[minIndex] = list[i]
		list[i] = itemToMove
	end = datetime.datetime.now()
	print 'it took ' + str(end - start) + ' to complete'
	print 'and %d if statements' % count
	return list

#print selection_sort(new_sample_list())
print selection_sort(new_big_sample_list())














