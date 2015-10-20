class TrieNode(object):
	def __init__(self, value = None):
		"""
		Initialize your data structure here.
		"""
		self.value = value
		self.children = {}
		
class Trie(object):

	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		if not word.islower():
			return False
			
		node = self.root
		
		for char in word:
			if char not in node.children:
				new_node = TrieNode(char)
				node.children[char] = new_node
				node = new_node
			else:
				node = node.children[char]
				
		# new_node.value = None

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		if not word.islower():
			return False
		
		node = self.root
		
		for char in word:
			if char not in node.children:
				return False
			else:
				node = node.children[char]
		
		if node.children:
			return False
		else:
			return True

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie
		that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		if not prefix.islower():
			return False
		
		node = self.root
		
		for char in prefix:
			if char not in node.children:
				return False
			
			else:
				node = node.children[char]
				
		return True
		
## Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("otherstring")
print trie.search("somestring")
print trie.startsWith("othersome")