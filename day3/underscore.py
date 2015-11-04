class underscore(object):
	def map(self, list, callback):
		new_list = []
		for elem in list:
			new_list.append(callback(elem))
		return new_list
	def find(self, list, predicate):
		for elem in list:
			if predicate(elem):
				return elem
		return
	def reduce(self, list, callback, start = None):
		if start == None:
			current = list[0]
			list = list[1:]
		else:
			current = start
		for elem in list:
			current = callback(current, elem)
		return current
	def filter(self, list, predicate):
		new_list = []
		for elem in list:
			if predicate(elem):
				new_list.append(elem)
		return new_list
	def reject(self, list, predicate):
		new_list = []
		for elem in list:
			if not predicate(elem):
				new_list.append(elem)
		return new_list

_ = underscore()

print _.map([1,2,3,4], lambda x: x*2) # double each element
print _.find([1,2,3,4], lambda x: x == 4) # find 4
print _.reduce([1,2,3,4], lambda start, x: start + x, 0) # add all, start at 0
print _.filter([1,2,3,4], lambda x: x % 2 == 0) # filter if even
print _.reject([1,2,3,4], lambda x: x % 2 == 0) # reject if even








