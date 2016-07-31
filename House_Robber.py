class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        if size==0:
            return 0

        if size==1:
            return nums[0]

        s = [0 for i in range(size)]
        s[0] = nums[0]
        s[1] = max(nums[0], nums[1])

        for i in xrange(2, size):
            s[i] = max(s[i-2]+nums[i], s[i-1])

        return s[-1]

sol = Solution()
n = [1,1,1]
print sol.rob(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        
        return max( self.do_rob(nums[1:]), self.do_rob(nums[:-1]) )
            
    def do_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
            
        size = len(nums)
        dp = [0, 0]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in xrange(2, size):
            dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2] + nums[i])
        
        return dp[(size-1)%2]
        