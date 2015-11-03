class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print 'Price: %s' % str(self.price)
		print 'Speed: %s' % str(self.speed)
		print 'Fuel: %s' % str(self.fuel)
		print 'Mileage: %s' % str(self.mileage)
		print 'Tax: %s\n\n' % str(self.tax)

car1 = Car(2000, '25mph', 'Full', '28mpg')
car2 = Car(1500, '20mph', 'Almost Empty', '19mpg')
car3 = Car(2500, '30mph', 'Full', '52mpg')
car4 = Car(1200, '10mph', 'Empty!', '12mpg')
car5 = Car(52000, '85mph', 'Full', '38mpg')






