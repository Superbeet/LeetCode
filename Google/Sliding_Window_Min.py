import collections

class Solution(object):
    def minSlidingWindow(self, nums, k):
		if nums == None or len(nums)==0:
			return []
		
		size = len(nums)
		queue = collections.deque()
		res = []
		
		for i in xrange(0, size):
			if len(queue) and queue[0]==i-k:
				queue.popleft()
			
			while len(queue) and nums[queue[-1]]>nums[i]:
				queue.pop()
			
			queue.append(i)
		
			if i>=k-1:
				res.append(nums[queue[0]])
		
		return res

sol = Solution()
nums = [3,2,1,-1,5,8,7]
k = 2
print sol.maxSlidingWindow(nums, k)