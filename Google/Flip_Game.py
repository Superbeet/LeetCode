class Solution(object):
    def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		size = len(s)
		if size==0:
			return []
		res = []
		for i in xrange(1, size):
			if s[i]=="+":
				if s[i-1]=="+":
					res.append(s[:i-1]+"--"+s[i+1:])
		return res

# sol = Solution()
# print sol.generatePossibleNextMoves("++++")
# print sol.generatePossibleNextMoves("--+++--")

# O(2^n)
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
		size = len(s)
		for i in xrange(0, size-1):
			if s[i]=='+' and s[i+1]=='+' and not self.canWin(s[:i]+"--"+s[i+2:]):
				return True
		return False
        