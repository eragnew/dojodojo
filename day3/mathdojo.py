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








