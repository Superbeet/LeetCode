class TrieNode:
	def __init__(self):
		self.children = dict()
		self.isWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for letter in word:
			if letter not in node.children:
				child = TrieNode()
				node.children[letter] = child
			else:
				child = node.children[letter]
			node = child
		node.isWord = True

	def delete(self, word):
		node = self.root
		queue = []
		for letter in word:
			queue.append((letter, node))
			child = node.children[letter]
			if child is None:
				return False
			node = child
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

	def startsWith(self, prefix):
		if not prefix.islower():
			return False
		node = self.root
		for char in prefix:
			if char not in node.children:
				return False
			else:
				node = node.children[char]
		return True
		
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
			
class Solution(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		res = []
		self.trie = Trie()
	
		def dfs(i, j, board, word, count):
			
			if count == len(word):
				if word not in res:
					res.append(word)
				return True
				
			if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
				return False
				
			# print "[i,j] [couunt] -> ", [i,j], [count]		
			
			if not self.trie.startsWith(word[:count+1]):
				return False
		
			if board[i][j] == '#':
				return False
			if board[i][j] != word[count]:
				return False
			temp = board[i][j]
			board[i][j] = '#'
			dfs(i-1, j, board, word, count+1)
			dfs(i+1, j, board, word, count+1)
			dfs(i, j+1, board, word, count+1)
			dfs(i, j-1, board, word, count+1)
			board[i][j] = temp
		
		for word in words:
			self.trie.insert(word)
			
			for i in xrange(len(board)):
				for j in xrange(len(board[0])):
					str = dfs(i, j, board, word, 0)

		return res
			
board = [
  ['o','a','a'],
  ['e','t','a'],
  ['i','h','k']
]
words = ["ath","ate"]
sol = Solution()
print sol.findWords(board, words)
		
		
			
