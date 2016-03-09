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
			
		for num in xrange(1, len(costs)):
			costs[num][0] = costs[num][0] + min(costs[i-1][1], costs[i-1][2])
			costs[num][1] = costs[num][1] + min(costs[i-1][0], costs[i-1][2])
			costs[num][2] = costs[num][2] + min(costs[i-1][0], costs[i-1][1])

		return min(costs[-1][0], costs[-1][1], costs[-1][2])
				

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