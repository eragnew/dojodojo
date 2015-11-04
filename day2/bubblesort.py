import random, datetime

# my first attempt

#arr = [6, 5, 3, 1, 8, 7, 2, 4]
#arr = [8, 7, 6, 5, 4, 3, 2, 1]

def new_sample_list():
	new_list = []
	for i in range(100):
		new_list.append(int(round(random.random() * 10000)))
	return new_list

def bubble_sort(list):
	start = datetime.datetime.now()
	done = False
	while not done:
		swaps_this_round = 0
		for i in range(len(list)):
			if i == len(list) - 1:
				continue
			else:
				if list[i] > list[i + 1]:
					valueToMove = list[i + 1]
					list[i + 1] = list[i]
					list[i] = valueToMove
					swaps_this_round += 1
		if swaps_this_round == 0:
			done = True
	end = datetime.datetime.now()
	print 'it took ' + str(end - start) + ' to complete'
	return list

print bubble_sort(new_sample_list())









