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