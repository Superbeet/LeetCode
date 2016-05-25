# BFS
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
        queue = collections.deque([beginWord, ""])
        
        while queue:       
            word = queue.popleft()     
            if word == endWord:
                return count
            if word == "" and queue:
                count += 1
                queue.append("")
            for i in xrange(0, len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + letter + word[i+1:]             
                    if new_word not in check and new_word in wordList:
                        check.add(new_word)
                        queue.append(new_word)
        return 0

# Double BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        forward, backward, count = set([beginWord]), set([endWord]), 2

        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            temp = set()
            for word in forward:
                wordList.discard(word)

            for word in forward:
                # word = forward.popleft()
                for i in xrange(len(word)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + letter + word[i + 1:]

                        if candidate in backward:
                            return count

                        if candidate in wordList:
                            # wordList.remove(candidate)
                            temp.add(candidate)

            forward = temp
            count += 1

        return 0

sol = Solution()

# bw = "a"
# ew = "c"
# wl = set(["a", "b", "c"])

bw = "hot"
ew = "dog"
wl = set(["hot","dog"])

print sol.ladderLength(bw, ew, wl)