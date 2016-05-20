class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        size = len(nums)
        
        # dp = [1 for i in range(size)]
        left_product = 1
        for i in xrange(0,size):
            dp[i] = left_product
            left_product = left_product * nums[i]
        
        # results = [0 for i in range(size)]
        right_product = 1
        for j in xrange(size-1, -1, -1):
            dp[j] = dp[j] * right_product
            right_product = right_product * nums[j]
            
        return dp