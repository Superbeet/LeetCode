import copy

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [ 0 for i in range(0, target+1) ]
        dp[0] = 1 # fetch nothing
        
        for i in xrange(target+1):
            for num in nums:
                if i + num > target:
                    continue
                dp[i + num] += dp[i]
                
        return dp[-1]
        
        
        
            
            