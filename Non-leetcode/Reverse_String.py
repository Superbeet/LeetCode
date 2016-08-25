# class Solution:
#     # @param s, a string
#     # @return a string
#     def reverseWords(self, s):
#         words = s.split()
#         words.reverse()
#         return " ".join(words)
        
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        res = ""
        size = len(s)
        j = size
        
        for i in xrange(size-1, -1, -1):
            if s[i] == " ":
                j = i
            elif i==0 or s[i-1]==" ":
                if res:
                    res += " "
                res += s[i:j]
        return res

s = "hello world"
sol = Solution()
print sol.reverseWords(s)