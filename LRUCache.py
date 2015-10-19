

class Node(object):
	def __init__(self, key=None, value=None):
		self.prev = None
		self.next = None
		self.key = key
		self.value = value

class LinkedList(object):
	def __init__(self):
		self.head = None	# Empty head node
		self.tail = None
		
	def isEmpty(self):
		return not self.tail
	
	def remove(self, node):
		# empty linkedlist
		if self.head == self.tail:
			self.head = None
			self.tail = None
			return
		
		if node == self.head:
			node.next.prev = None
			self.head = node.next
			return
			
		if node == self.tail:
			node.prev.next = None
			self.tail = node.prev
			return
		
		node.prev.next = node.next
		node.next.prev = node.prev
	
	def remove_tail(self):
		self.remove(self.tail)
	
	def add_tail(self, node):
		
		if not self.tail:
			self.head = node
			self.tail = node
		
		else:
			node.next = None
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
	
	def add_head(self, node):
		
		if not self.head:
			self.head = node
			self.tail = node
			node.next = None
			node.prev = None
			
		else:
			node.next = self.head
			node.prev = None
			self.head.prev = node
			self.head = node

	def traverse(self):
		node = self.head
		res = []

		while node:
			res.append(str([node.key, node.value]))
			node = node.next

		res_str = " -> ".join(res)
		print res_str


class LRUCache(object):
	
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity
		self.size = 0	# current size
		self.hash_map = {}
		self.cache = LinkedList()

	def get(self, key):
		"""
		:rtype: int
		"""
		if key in self.hash_map and self.hash_map[key]:
			self.cache.remove(self.hash_map[key])
			self.cache.add_head(self.hash_map[key])
			return self.hash_map[key].value
			
		else:
			return -1

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if key in self.hash_map:
			self.cache.remove(self.hash_map[key])
			self.cache.add_head(self.hash_map[key])
			self.hash_map[key].value = value
			
		else:
			node = Node(key,value)
			self.cache.add_head(node)
			self.hash_map[key] = node
			
			self.size += 1
			
			if self.size > self.capacity:
				self.size -= 1
				del self.hash_map[self.cache.tail.key]
				self.cache.remove_tail()

def debugger():
	print "*****************"
	sol.cache.traverse()
	print sol.hash_map
	print "*****************"

sol = LRUCache(10)

sol.set(10,13)
sol.set(3,17)
sol.set(6,11)
sol.set(10,5)
sol.set(9,10)
sol.get(13)
sol.set(2,19)
debugger()
sol.get(2)
debugger()
sol.get(3)
sol.set(5,25)
sol.get(8)
debugger()
sol.set(9,22)
sol.set(5,5)
sol.set(1,30)
sol.get(11)
debugger()
sol.set(9,12)
sol.get(7)
sol.get(5)
sol.get(8)
sol.get(9)
debugger()
sol.set(4,30)
sol.set(9,3)
sol.get(9)
sol.get(10)
sol.get(10)
sol.set(6,14)
sol.set(3,1)
sol.get(3)
sol.set(10,11)
sol.get(8)
sol.set(2,14)
sol.get(1)
sol.get(5)
sol.get(4)
sol.set(11,4)
sol.set(12,24)
sol.set(5,18)
sol.get(13)
debugger()
sol.set(7,23)

sol.get(8)
sol.get(12)
sol.set(3,27)
sol.set(2,12)
sol.get(5)
sol.set(2,9)
sol.set(13,4)
sol.set(8,18)
sol.set(1,7)
sol.get(6)
sol.set(9,29)
sol.set(8,21)
sol.get(5)
sol.set(6,30)
sol.set(1,12)
sol.get(10)
sol.set(4,15)
sol.set(7,22)
sol.set(11,26)
sol.set(8,17)
sol.set(9,29)
sol.get(5)
sol.set(3,4)
sol.set(11,30)
sol.get(12)
sol.set(4,29)
sol.get(3)
sol.get(9)
sol.get(6)
sol.set(3,4)
sol.get(1)
sol.get(10)
sol.set(3,29)
sol.set(10,28)
sol.set(1,20)
sol.set(11,13)
sol.get(3)
sol.set(3,12)
sol.set(3,8)
sol.set(10,9)
sol.set(3,26)
sol.get(8)
sol.get(7)
sol.get(5)
sol.set(13,17)
sol.set(2,27)
sol.set(11,15)
sol.get(12)
sol.set(9,19)
sol.set(2,15)
sol.set(3,16)
sol.get(1)
sol.set(12,17)
sol.set(9,1)
sol.set(6,19)
sol.get(4)
sol.get(5)
sol.get(5)
sol.set(8,1)
sol.set(11,7)
sol.set(5,2)
sol.set(9,28)
sol.get(1)
sol.set(2,2)
sol.set(7,4)
sol.set(4,22)
sol.set(7,24)
sol.set(9,26)
sol.set(13,28)
sol.set(11,26)

# sol.set(2,1)
# sol.set(2,2)
# sol.get(2)
# sol.set(1,1)
# sol.set(4,1)
# sol.cache.traverse()
# print sol.hash_map
# sol.get(2)
