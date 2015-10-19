
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        n = len(s)+1
        possible = [False] * n

        for i in xrange(1, n):

        	if s[0:i] in wordDict:
        		
        		possible[i] = True

      		else:

      			for j in xrange(0, i):

      				if possible[j] and s[j:i] in wordDict:

      					possible[i] = True

      					break

      	return possible[n-1]


sol = Solution()
s = "leetcode"
s = "ab"
word_dict = {"leet":0, "code":1, "hello":2, "venus":3, "future":4}
word_dict = ["a","b"]
print sol.wordBreak(s, word_dict)
