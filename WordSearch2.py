class TrieNode(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.isWord = True
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
				new_node = TrieNode()
				node.children[char] = new_node
				node = new_node
			else:
				node = node.children[char]

		node.isWord = True

	def delete(self, word):
		node = self.root
		queue = []

		for letter in word:
			queue.append((letter, node))

			if letter not in node.children:
				return False
			else:
				node = node.children[letter]

		if not node.isWord:
			return False

		if len(node.children):
			node.isWord = False

		else:
			for letter, node in queue[::-1]:
				del node.children[letter]
				if len(node.children) or node.isWord:
					break
		return True




			