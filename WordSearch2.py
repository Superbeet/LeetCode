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


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
    def dfs(self, word, node, x, y)