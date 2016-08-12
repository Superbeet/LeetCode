class Solution:
    def wordBreak(self, s, dict):
        # write your code here
        # dp[i] => True/False if 0...i can be broke into words
        # dp[i] = dp[j] and s[j+1:i] is a word
        # dp[0] = False
        if not s:
            return True
        
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in xrange(1, len(s)+1):
            for j in xrange(0, i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
                
        return dp[len(s)]

"""
Pruning short and long candidate string comparsion
"""
class Solution:
    def wordBreak(self, s, dict):
        # write your code here
        # dp[i] => True/False if 0...i can be broke into words
        # dp[i] = dp[j] and s[j+1:i] is a word
        # dp[0] = False
        if not s:
            return True
        
        max_len = -sys.maxint
        min_len =  sys.maxint
        
        for word in dict:
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))
        
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in xrange(1, len(s)+1):
            for j in xrange(max(0, min_len), min(i, max_len) + 1):  # width
            
                if dp[i - j] and s[i - j:i] in dict:
                    dp[i] = True
                    break
                
        return dp[len(s)]
        
