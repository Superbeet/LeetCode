# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4]
the contiguous subarray [4,−1,2,1] has the largest sum = 6
"""
# O(n) time O(n) space
import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        sum_val = 0
        max_val = -sys.maxint
        for i in xrange(0, len(nums)):
            sum_val = (dp[i-1] if dp[i-1]>0 else 0) +nums[i]
            dp[i] = sum_val
        return max(dp)

# Path compression
# O(n) time O(1) space
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_val = 0
        max_val = -sys.maxint
        for i in xrange(0, len(nums)):
            sum_val += nums[i]
            if sum_val>max_val:
                max_val = sum_val
            if sum_val<0:
                sum_val = 0
        return max_val

# nlog(n) time O(1) space
import sys
MinInt = -sys.maxint
class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		size = len(nums)
		return self.max_sub_array(nums, 0, size-1, MinInt)

	def max_sub_array(self, nums, left, right, max_val):
		if left>right:
			return MinInt
		mid = (left + right)/2
		# In left part
		l_max = self.max_sub_array(nums, left, mid-1, max_val)
		# In right part
		r_max = self.max_sub_array(nums, mid+1, right, max_val)
		# Cross two parts
		sum_val, l_part_max = 0, 0
		for i in xrange(mid-1, left-1, -1):
			sum_val += nums[i]
			l_part_max = max(l_part_max, sum_val)

		sum_val, r_part_max = 0, 0
		for j in xrange(mid+1, right+1):
			sum_val += nums[j]
			r_part_max = max(r_part_max, sum_val)

		max_val = max(max_val, l_max, r_max, l_part_max + nums[mid] + r_part_max)
		return max_val
		
		
		
		
		
		
		
		
		
		
		
		