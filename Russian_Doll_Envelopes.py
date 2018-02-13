"""
Input
[[5,4],[6,4],[6,7],[2,3]]

Sorted
[[2, 3], [5, 4], [6, 7], [6, 4]]

DP
[[2, 3]]
[[2, 3], [5, 4]]
[[2, 3], [5, 4], [6, 7]]
[[2, 3], [6, 4], [6, 7]]

"""

import copy
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        nums = sorted(envelopes, cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        
        size = len(nums)
        dp = []
        
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low + 1 < high:
                mid = (low + high) / 2
                if dp[mid][1] == nums[x][1]:
                    high = mid
                if dp[mid][1] < nums[x][1]:
                    low = mid
                else:
                    high = mid
                    
            if 0 <= low < len(dp) and dp[low][1] >= nums[x][1]:
                dp[low] = nums[x]
            elif 0 <= high < len(dp) and dp[high][1] >= nums[x][1]:
                dp[high] = nums[x]
            else:
                dp.append(nums[x])

        return len(dp)

import copy

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        # envelopes = sorted(envelopes)
        # print envelopes
        
        size = len(envelopes)
        self.res = []
        memo = {}
        max_sum = self.get_max_num(envelopes, -1, memo)
        return max_sum
        
    def get_max_num(self, envelopes, top, memo):
        if top in memo:
            return memo[top]

        if top >= len(envelopes):
            return 0
        
        max_size = 0
        for j in xrange(0, len(envelopes)):
            if self.can_fit(envelopes, top, j):
                cur_size = self.get_max_num(envelopes, j, memo) + 1
                max_size = max(max_size, cur_size)
        
        memo[top] = max_size
                
        return max_size
        
    def can_fit(self, envelopes, i, j):
        if i == -1:
            return True
            
        if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
            return True
        
        return False