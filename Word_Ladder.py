import collections 

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        count = 1
        check = set()
        queue = collections.deque()
        
        queue.append(beginWord)
        
        while queue:
            
            word = queue.popleft()
            
            if word == endWord:
                return count
                
            for i in xrange(0, len(word)):
                for asc in xrange(97, 97+26):
                    word = word[:i] + chr(asc) + word[i+1:]
            
                    if word == "" and queue:
                        count += 1
                        queue.append("")
                    
                    if word not in check and word in wordList:
                        check.add(word)
                        queue.append(word)
        
        return 0

bw = "a"
ew = "c"
wl = ["a", "b", "c"]

sol = Solution()
print sol.ladderLength(bw, ew, wl)