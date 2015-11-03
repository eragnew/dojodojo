def print1to255():
	for i in range(1, 256):
		print i
#print1to255()

def printOdds1to255():
	for i in range(1, 256):
		if i % 2 != 0:
			print i
#printOdds1to255()

def printIntsAndSum0To255():
	sum = 0
	for i in range(256):
		sum += i
		print i, sum
#printIntsAndSum0To255()

def printArrayVals(arr):
	for i in arr:
		print i
#printArrayVals([1,2,3])

def printMaxOfArray(arr):
	max = 0
	for i in arr:
		if i > max:
			max = i
	print max
#printMaxOfArray([10,2,3,4,5])

def printAverageOfArray(arr):
	total = 0
	for i in arr:
		total += i
	print total / len(arr)
#printAverageOfArray([1,2,3])

def returnOddsArray1To255():
	arr = []
	for i in range(1, 256):
		if i % 2 != 0:
			arr.append(i)
	return arr
#print returnOddsArray1To255()

def squareArrayVals(arr):
	new_arr = []
	for i in arr:
		new_arr.append(i * i)
	return new_arr
#print squareArrayVals([1,2,3,4])

def returnArrayCountGreaterThanY(arr, y):
	count = 0
	for i in arr:
		if i > y:
			count += 1
	return count
#print returnArrayCountGreaterThanY([1,2,3,4], 0)

def zeroOutArrayNegativeVals(arr):
	new_arr = []
	for i in arr:
		if i < 0:
			new_arr.append(0)
		else:
			new_arr.append(i)
	return new_arr
#print zeroOutArrayNegativeVals([-1,0,2,-3,3])

def printMaxMinAverageArrayVals(arr):
	max, min, total = arr[0], arr[0], 0
	for i in arr:
		total += i
		if i > max:
			max = i
		if i < min:
			min - i
	print max, min, total / len(arr)
#printMaxMinAverageArrayVals([1,2,3,4])

# [1,2,3,4]
# [2,3,4,0]

def shiftArrayValsLeft(arr):
	new_arr = arr[1:]
	new_arr.append(0)
	return new_arr
#print shiftArrayValsLeft([1,2,3,4])

def swapStringForArrayNegativeVals(arr):
	new_arr = []
	for i in arr:
		if i < 0:
			new_arr.append('Dojo')
		else:
			new_arr.append(i)
	return new_arr
#print swapStringForArrayNegativeVals([1,-1,3,5,-2])

















