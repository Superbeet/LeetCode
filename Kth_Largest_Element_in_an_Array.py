# Use Bubble k times - Time Complexity: O(nk)
class Solution3(object):
	def findKthLargest(self, nums, k):
		if not nums:
			return None
		size = len(nums)
		for i in xrange(0, k):
			for j in xrange(0, size-1-i):
				if nums[j]>nums[j+1]:
					nums[j],nums[j+1] = nums[j+1], nums[j]
		
		return nums[-k]
		
# Time complexity: O(k + (n-k)Logk) <~> O(nlogk)
import heapq
class MinHeap(object):
	def __init__(self, k):
		self.k = k
		self.data = []
	
	def push(self, element):
		if len(self.data)<self.k:
			heapq.heappush(self.data, element)
		else:
			if element>self.data[0]:
				heapq.heapreplace(self.data, element)
	
	def pop(self):
		return heapq.heappop(self.data)

class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		if not nums:
			return None

		size = len(nums)
		heap = MinHeap(k)

		for i in xrange(0, size):
			heap.push(nums[i])

		return heap.pop()

# Time: O(n+klogn)
class MaxHeap(object):
	def __init__(self, k):
		self.k = k
		self.data = []
	
	def push(self, element):
		element = -element
		if len(self.data)<self.k:
			heapq.heappush(self.data, element)
		else:
			if element>self.data[0]:
				heapq.heapreplace(self.data, element)
	
	def pop(self):
		return -heapq.heappop(self.data)

class Solution2(object):
	def findKthLargest(self, nums, k):
		if not nums:
			return None

		size = len(nums)
		heap = MaxHeap(size)
		
		for i in xrange(0, size):
			heap.push(nums[i])
		
		for j in xrange(k-1):
			heap.pop()
		
		return heap.pop()
		
sol = Solution()
sol2 = Solution2()
sol3 = Solution3()
nums = [3,2,1,5,6,4,11,8,7] 
print sol.findKthLargest(nums, 2)
print sol2.findKthLargest(nums, 2)
print sol3.findKthLargest(nums, 2)

