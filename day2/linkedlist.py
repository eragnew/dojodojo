class Node(object):
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

class DoublyLinkedList(object):
	def __init__(self):
		self._length = 0
		self.head = None
		self.tail = None
	def addNode(self, value):
		node = Node(value)
		if self._length:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
		else:
			self.head = node
			self.tail = node
		self._length += 1
		return node
	def removeNode(self, position):
		currentNode = self.head
		length = self._length
		count = 1
		beforeNodeToDelete, nodeToDelete, deletedNode, afterNodeToDelete = None, None, None, None
		if length == 0 or position < 1 or position > length:
			print 'Invalid position given to removeNode!'
			return
		if position == 1:
			self.head = currentNode.next
			if not self.head:
				self.head.prev = None
			else:
				self.tail = None
		elif position == self._length:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			while count < position:
				currentNode = currentNode.next
				count += 1
			beforeNodeToDelete = currentNode.prev
			nodeToDelete = currentNode
			afterNodeToDelete = currentNode.next
			beforeNodeToDelete.next = afterNodeToDelete
			afterNodeToDelete.prev = beforeNodeToDelete
			deletedNode = nodeToDelete
			nodeToDelete = None
		self._length -= 1













