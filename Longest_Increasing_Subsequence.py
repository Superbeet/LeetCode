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

sol = Solution()
print sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])