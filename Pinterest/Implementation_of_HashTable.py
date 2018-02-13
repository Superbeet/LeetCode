"""
Realize Hashtable

Two arrays:
1. key_list[key] = pointer to value obj
2. value_list[key] = node -> chaining -> [key1, val1] -> [key2, val2]

Assuming, that hash function distributes hash codes uniformly and table allows dynamic 
resizing, amortized complexity of insertion, removal and lookup operations is constant. 

HashSet is simpler version of HashMap

Set() - Hash or Linear

time complexity
- put
- get
- remove
- contains

Skip duplicate

"""
class LinkedHashEntry():
	def __init__(self, key = None, value = None):
		self.key = key
		self.value = value
		self.next = None

class HashTable():
	def __init__(self, size = None):
		if size is None:
			self.size = 1000
		self.load = 0
		self.table = [None for i in xrange(self.size)]

	def hash(self, key, size):
		char_sum = 0
		for c in str(key):
			char_sum += ord(c)

		hash_code = char_sum % size
		# print "hash_code ->", hash_code
		return hash_code

	def put(self, key, value):
		hash_key = self.hash(key, self.size)

		if self.table[hash_key] is None:
			self.table[hash_key] = LinkedHashEntry(key, value)
			self.load += 1
		else:
			entry = self.table[hash_key]
			while entry.next is not None and entry.key != key:
				entry = entry.next

			if entry.key == key:
				entry.value = value
			else:
				entry.next = LinkedHashEntry(key, value)
				self.load += 1

		self.resize()

	def get(self, key):
		hash_key = self.hash(key, self.size)

		if self.table[hash_key] is None:
			return -1

		else:
			entry = self.table[hash_key]

			while entry.next is not None and entry.key != key:
				entry = entry.next

			if entry.key == key:
				return entry.value
			else:
				return -1

	def delete(self, key):
		hash_key = self.hash(key, self.size)

		if self.table[hash_key] is None:
			return -1

		else:
			entry = self.table[hash_key]
			prev = None

			while entry.next is not None and entry.key != key:
				prev = entry
				entry = entry.next

			if entry.key == key:
				
				if prev is None:
					self.table[hash_key] = entry.next
				else:
					prev.next = entry.next

				self.load -= 1
				return entry.value

			else:
				return -1

	def get_load_factor(self):
		factor = self.load/float(self.size)
		print "factor ->", factor
		return factor

	def resize(self):

		def put_entry(key, new_entry):
			if new_table[key] is None:
				new_table[key] = new_entry
			else:
				entry = new_table[key]
				while entry.next is not None:
					entry = entry.next
				entry.next = new_entry
			return

		factor = self.get_load_factor()
		self.size = len(self.table)

		if factor < 0.01 and factor >= 0.001:
			return
		elif factor >= 0.01:
			new_size = 2 * self.size
			print "rehashing to 2x"
		else:
			new_size = int(0.5 * self.size)
			print "rehashing to 1/2"

		# new_size = 2 * self.size
		new_table = [None for i in xrange(new_size)]

		for head in self.table:
			if head is None:
				continue
			i = self.hash(head.key, new_size)
			entry = head
			while entry is not None:
				new_key = self.hash(entry.key, new_size)
				put_entry(new_key, head)
				entry = entry.next

		self.table = new_table
		self.size = new_size

ht = HashTable()
ht.put(3, 3)
ht.put(2, 2)
ht.put(5, 5)
ht.put(6, 6)
ht.put(1, 1)
ht.put(7, 7)
ht.put(8, 8)
ht.put(9, 9)

print ht.get(3) == 3
print ht.get(2) == 2

ht.put(10, 10)
ht.put(11, 11)
ht.put(12, 12)


print ht.get(2) == 2
print ht.get(3) == 3

ht.put(3,33)
ht.put(2,22)
# assert ht.get(3) == 33
# assert ht.get(2) == 22
print ht.get(3) == 33
print ht.get(2) == 22

print ht.delete(5)
print ht.delete(3)
print ht.delete(5)
print "----------"
print ht.get(3)
print ht.get(5)

# class LinkedHashEntry():
# 	def __init__(self, key = None, value = None):
# 		self.key = key
# 		self.value = value
# 		self.next = None

# 	def get_value(self):
# 		return self.value

# 	def set_value(self, value):
# 		self.value = value

# 	def get_key(self):
# 		return self.key

# 	def get_next(self):
# 		return self.next

# 	def set_next(self, next):
# 		self.next = next

# class HashTable():
# 	def __init__(self):
# 		self.table_size = 128
# 		self.table = [None for i in range(self.table_size)]

# 	def hash(self, key, size):
# 		return sum([ord(c) for c in key_str]) % self.size

# 	def get(self, key):
# 		hash_key = self.hash(key)

# 		if self.table[hash_key] is None:
# 			return -1

# 		else:
# 			entry = self.table[hash_key]

# 			while entry is not None and entry.get_key() is not key:
# 				entry = entry.get_next()

# 			if entry.get_key() == key:
# 				return entry.get_value()
# 			else:
# 				return -1

# 	def put(self, key, value):
# 		hash_key = self.hash(key)

# 		if self.table[hash_key] is None:
# 			self.table[hash_key] = LinkedHashEntry(key, value)
# 		else:
# 			entry = self.table[hash_key]

# 			while entry.get_next() is not None and entry.get_key() != key:
# 				entry = entry.get_next()

# 			if entry.get_key() == key:
# 				return entry.get_value()
# 			else:
# 				return -1

# 	def delete(self, key):
# 		hash_key = self.hash(key)

# 		if self.table[hash_key] is None:
# 			return -1

# 		else:
# 			entry = self.table[hash_key]
# 			prev = None

# 			while entry.get_next() is not None and entry.get_key() != key:
# 				prev = entry
# 				entry = entry.get_next()

# 			if entry.get_key() == key:
# 				if prev is None:
# 					self.hash[hash_key] = entry.get_next()
# 				else:
# 					prev.set_next(entry.get_next())







