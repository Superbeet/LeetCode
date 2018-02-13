class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, val):
        node = self.root
        
        for letter in val:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        
        node.is_word = True
        
class Solution(object):
    def findWords(self, board, words):
        # write your code here
        if not board:
            return []
        
        h = len(board)
        w = len(board[0])
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        result = []
        
        for j in xrange(h):
            for i in xrange(w):
                self.dfs(board, trie.root, w, h, i, j, "", result)
        
        return sorted(result)
        
    def dfs(self, board, node, m, n, x, y, word, result):
        if node.is_word:
            result.append(word)
            node.is_word = False
            
        if x < 0 or x >= m or y < 0 or y >= n:
            return 
        
        curr = board[y][x]
        
        if curr == "#":
            return 
        
        if curr not in node.children:
            return
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for nx, ny in dirs:
            dx = x + nx
            dy = y + ny
            board[y][x] = "#"
            self.dfs(board, node.children[curr], m, n, dx, dy, word + curr, result)
            board[y][x] = curr
    