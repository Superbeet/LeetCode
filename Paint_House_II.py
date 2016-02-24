"""
265. Paint House II My Submissions Question [Hard]
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
"""
import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
        	return 0
        	
        pre_min, pre_sec, pre_idx = 0, 0, -1
        
        for i in xrange(0, len(costs)):
        	cur_min, cur_sec, cur_idx= sys.maxint, sys.maxint,-1
        	for j in xrange(0, len(costs[0])):
        		temp_cost = costs[i][j] + (pre_sec if pre_idx==j else pre_min)
        		
        		if temp_cost<cur_min:
        			cur_sec = cur_min
        			cur_min = temp_cost
        			cur_idx = j
        		
        		elif temp_cost<cur_sec:
        			cur_sec = temp_cost
        	
        	pre_min = cur_min
        	pre_sec = cur_sec
        	pre_idx = cur_idx
        
        return pre_min