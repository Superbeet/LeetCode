class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or len(nums)==0:
            return nums

        result = []
        queue = []

        size = len(nums)

        for i in xrange(0, size):
            if len(queue) and queue[0]==i-k:
                queue.pop(0)

            while len(queue) and nums[queue[-1]]<nums[i]:
                queue.pop(-1)

            queue.append(i)


            if i >= k-1:
                result.append(nums[queue[0]])

        return result