class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class DoubleLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def add(self, value):
		node = Node(value)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
	def find(self, value):
		curr = self.head
		while curr.value != value:
			curr = curr.next
		return curr
	def remove(self, value):
		curr = self.head
		while curr.value != value:
			curr = curr.next
		if curr:
			curr.prev.next = curr.next
			curr.next.prev = curr.prev
			return curr
	def insert(self, value, matchValue):
		node = Node(value)
		curr = self.head
		while curr.value != matchValue:
			curr = curr.next
		if curr:
			movedNode = curr.next
			curr.next = node
			node.prev = curr
			node.next = movedNode
			movedNode.prev = node
	def printNodes(self):
		if self.head:
			curr = self.head
			print curr.value
			while curr.next:
				print curr.value















