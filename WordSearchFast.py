

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ""
        self.word = False
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
        child = self.root
        for letter in word:
            if letter not in child.children:
                child.children[letter] = TrieNode()
            child = child.children[letter]
        child.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        child = self.root
        for letter in word:
            if letter in child.children:
                child = child.children[letter]
            else:
                return False
        return child.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        child = self.root
        for letter in prefix:
            if letter in child.children:
                child = child.children[letter]
            else:
                return False
        return True
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Postprocessing
        trie = Trie()
        for word in words:
        	trie.insert(word)
        # DFS from each position
        self.res = set()
        for i in xrange(len(board)):
        	for j in xrange(len(board[i])):
        		# visited = set()
        		self.dfs(board, trie.root, i, j, "")
        return list(self.res)

    def dfs(self, board, trie, i, j, str):
    	if i<0 or i>=len(board) or j<0 or j>=len(board[i]):
    		return
    	if board[i][j] == '#':
    		return
    	cur = board[i][j]
    	if cur in trie.children:
    		if trie.children[cur].word:
    			self.res.add(str+cur)
    		board[i][j] = '#'
    		self.dfs(board, trie.children[cur], i+1, j, str+cur)
    		self.dfs(board, trie.children[cur], i-1, j, str+cur)
    		self.dfs(board, trie.children[cur], i, j+1, str+cur)
    		self.dfs(board, trie.children[cur], i, j-1, str+cur)
    		board[i][j] = cur
    	else:
    		return

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
sol = Solution()
print sol.findWords(board, words)