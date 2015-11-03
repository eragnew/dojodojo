class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: $%s' % str(self.price)
		print 'Maximum Speed: %s' % str(self.max_speed)
		print 'Total Miles Ridden: %s' % str(self.miles)
	def ride(self):
		print 'Riding...'
		self.miles += 10
	def reverse(self):
		print 'Reversing...'
		if self.miles >= 5:
			self.miles -= 5

bike1 = Bike(200, '25mph')
bike2 = Bike(300, '30mph')
bike3 = Bike(120, '20mph')

print 'bike1:'
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

print '\nbike2:'
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

print '\nbike3:'
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()





