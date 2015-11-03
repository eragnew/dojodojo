class Animal(object):
	def __init__(self, name = 'animal'):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print 'Name: %s' % self.name
		print 'Health: %s\n\n' % str(self.health)

animal = Animal()
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

dog = Dog('Fido the Dog')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print 'this is a dragon!'
		super(Dragon, self).displayHealth()

dragon = Dragon('Aragon the Dragon')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

try:
	animal.fly()
except:
	print 'animal.fly() failed as expected...'

try:
	animal.pet()
except:
	print 'animal.pet() failed as expected...'







