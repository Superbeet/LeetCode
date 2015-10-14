

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
			return None
		
		if node == self.head:
			node.next.prev = None
			node.next.key = None
			node.next.value = None
			self.head = node.next
			return None
			
		if node == self.tail:
			node.prev.next = None
			node.prev.key = None
			node.prev.value = None
			self.tail = node.prev
			return None
		
		node.prev.next = node.next
		node.next.prev = node.prev
		
		return node
	
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
			return False

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
				self.cache.remove_tail()
				print self.hash_map
				del self.hash_map[self.cache.tail.key]
			
sol = LRUCache(1)
sol.set(2,1)
sol.get(2)
sol.set(3,2)
sol.get(2)
sol.get(3)

