# beat 20%
class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix:
			return 0

		m, n = len(matrix), len(matrix[0])
		dp = [[0 for i in range(n)] for j in range(m)]
		res = 0
		
		for j in xrange(m):
			dp[j][0] = int(matrix[j][0])
			res = max(res, dp[j][0])
			
		for i in xrange(n):
			dp[0][i] = int(matrix[0][i])
			res = max(res, dp[0][i])
			
		for j in xrange(1, m):
			for i in xrange(1, n):
				if matrix[j][i]=="1":
					dp[j][i] = min(dp[j-1][i],dp[j][i-1],dp[j-1][i-1]) + 1
					res = max(res, dp[j][i])

		return res*res

def printMtx(matrix):
	for row in matrix:
		print row
	print ""
		
sol = Solution()
print sol.maximalSquare(["11","11"])
