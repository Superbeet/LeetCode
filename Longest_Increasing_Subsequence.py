# O(n^2)
class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        size = len(nums)
        
        dp = [1 for i in range(size)]
        
        for i in xrange(1, size):
            for j in xrange(0, i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
        
        return max(dp)

    def val_of_LIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        size = len(nums)
        
        dp = [1 for i in range(size)]
        path = [j for j in range(size)]

        for i in xrange(1, size):
            for j in xrange(0, i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
                    path[i] = j
        
        max_val = 0
        for index, val in enumerate(nums):
            if val>max_val:
                max_val = val
                max_index = index

        res = []
        index = max_index
        prev = 0
        while index!=prev:
            res.append(nums[index])
            prev = index
            index = path[prev]
        
        return res[::-1]

#O(nlog(n))
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        
        dp = [nums[0]]
        
        for i in xrange(1, size):
            if nums[i]>dp[-1]:
                dp.append(nums[i])
            else:
                start, end = 0, len(dp)-1
                # print dp
                while start<=end:
                    mid = (start+end)/2
                    # print mid
                    if dp[mid]<nums[i]:
                        start = mid+1
                    else:
                        end = mid-1
                dp[start] = nums[i]
        
        return len(dp)

sol = Solution1()
# print sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
# print sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
print sol.val_of_LIS([10, 9, 2, 5, 3, 7, 101, 18])