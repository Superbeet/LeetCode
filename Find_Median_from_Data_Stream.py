# Time: addNum -> O(log(n)), findMedian -> O(1) Space: O(n)
from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.minheap = []
		self.maxheap = []

    def addNum(self, num):
		"""
		Adds a num into the data structure.
		:type num: int
		:rtype: void
		"""
		heappush(self.maxheap, -num)
		min_top = self.minheap[0] if len(self.minheap) else None
		max_top = self.maxheap[0] if len(self.maxheap) else None

		if (min_top and max_top) and min_top<-max_top or len(self.minheap)<len(self.maxheap)-1:
			heappush(self.minheap, -heappop(self.maxheap))

		if len(self.maxheap)<len(self.minheap):
			heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self):
		"""
		Returns the median of current data stream
		:rtype: float
		"""
		if len(self.minheap)<len(self.maxheap):
			return -self.maxheap[0]
		else:
			return (self.minheap[0]-self.maxheap[0])/2.0

"""
Q：如果要求第n/10个数字该怎么做？
A：改变两个堆的大小比例，当求n/2即中位数时，两个堆是一样大的。而n/10时，说明有n/10个数小于目标数，9n/10个数大于目标数。所以我们保证最小堆是最大堆的9倍大小就行了。
"""
			
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()