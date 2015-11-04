class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, param1, *params):
		self.result += param1
		if params:
			for i in params:
				self.result += i
		return self
	def subtract(self, param1, *params):
		self.result -= param1
		if params:
			for i in params:
				self.result -= i
		return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

class MathDojo2(object):
	def __init__(self):
		self.result = 0
	def add(self, param1, *params):
		for i in param1:
			self.result += i
		if params:
			for i in params[0]:
				self.result += i
		return self
	def subtract(self, param1, *params):
		sub1 = 0
		for i in param1:
			sub1 += i
		self.result -= sub1
		if params:
			sub2 = 0
			for i in params[0]:
				sub2 += i
			self.result -= sub2
		return self

md2 = MathDojo2()
print md2.add([1]).add([3,5,7,8], [2,4.3,1.25]).subtract([2,3], [1.1,2.3]).result

class MathDojo3(object):
	def __init__(self):
		self.result = 0
	def add(self, param1, *params):
		if type(param1) == (list or tuple):
			for i in param1:
				self.result += i
			if params:
				for i in params[0]:
					self.result += i
		else:
			self.result += param1
			if params:
				for i in params:
					self.result += i
		return self
	def subtract(self, param1, *params):
		if type(param1) == (list or tuple):
			sub1 = 0
			for i in param1:
				sub1 += i
			self.result -= sub1
			if params:
				sub2 = 0
				for i in params[0]:
					sub2 += i
				self.result -= sub2
		else:
			self.result -= param1
			if params:
				for i in params:
					self.result -= i
		return self

md3 = MathDojo3()
print md3.add(1).add(2,3).subtract(3).result

md4 = MathDojo3()
print md4.add([1]).add([2,3]).subtract([3]).result







