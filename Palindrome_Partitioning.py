import copy

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if s is None or s == "":
            return []
        
        result = []
        self.build_palindrome_partition(s, 0, [], result)        
        return result
        
    def build_palindrome_partition(self, s, start, ans, res):
        if start >= len(s):
            res.append(copy.deepcopy(ans))
            return
        
        for i in xrange(start+1, len(s)+1):
            if self.is_palindrome(s[start:i]):
                ans.append(s[start:i])
                self.build_palindrome_partition(s, i, ans, res)
                ans.pop()
        
    def is_palindrome(self, s):
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True