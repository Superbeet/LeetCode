"""
Support search patterns
"." - any character
"*" - any number of former characters
corner case - .*.*
"""
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.adj = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        
        for char in word:
            if char not in node.adj:
                node.adj[char] = TrieNode()
            node = node.adj[char]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(node, word):

            if word=="":
                return node.is_word

            if len(word)==1 or word[1]!='*':
                if word[0]==".":
                    for char in node.adj:
                        if find(node.adj[char], word[1:]):
                            return True
                    return False
                    
                elif word[0] in node.adj:
                    return find(node.adj[word[0]], word[1:])

            else:    #word[1]=='*'
                
                while node.adj:
                    if word[0] == '.':
                        for char in node.adj:
                            if find(node.adj[char], word[2:]):
                                return True
                        node = node.adj[char]
                        
                    elif (word[0] in node.adj):
                        if find(node.adj[word[0]], word[2:]):
                            return True
                        node = node.adj[word[0]]
                    
                    else:
                        break
                        
                return False
                        
            return False
            
        return find(self.root, word)
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("pattern")
print wordDictionary.search("patte.n")
print wordDictionary.search("pa..e.n")
print wordDictionary.search("pat*ern")
print wordDictionary.search(".*.*n")

class WordDictionary2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        
        for char in word:
            if char not in node.adj:
                node.adj[char] = TrieNode()
            node = node.adj[char]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(node, word):
            
            if word=="":
                return node.is_word
            
            if word[0]==".":
                for char in node.adj:
                    if find(node.adj[char], word[1:]):
                        return True
                
            elif word[0] in node.adj:
                return find(node.adj[word[0]], word[1:])
            
            return False
            
        return find(self.root, word)