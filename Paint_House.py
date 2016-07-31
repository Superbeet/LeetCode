"""
256. Paint House [Medium]

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
"""

class Solution(object):
    def minCost(self, costs):
		"""
		:type costs: List[List[int]]
		:rtype: int
		"""
		if not costs:
			return 0
		
		dp = [[-1 for i in xrange(len(costs[0]))] for i in xrange(len(costs))]
		dp[0][0] = costs[0][0]
		dp[0][1] = costs[0][1]
		dp[0][2] = costs[0][2]
		
		for i in xrange(1, len(costs)):
			dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
			dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1] 
			dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

		return min(dp[-1][0], dp[-1][1], dp[-1][2])

class Solution(object):
    def minCost(self, costs):
		"""
		:type costs: List[List[int]]
		:rtype: int
		"""
		if not costs:
			return 0
			
		for num in xrange(0, len(costs)):
			r, g, b = rr, gg, bb
			bb = costs[num][0] + min(r, g)
			gg = costs[num][1] + min(r, b)
			rr = costs[num][2] + min(g, b)

		return min(bb, gg, rr)