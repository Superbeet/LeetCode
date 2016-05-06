from heapq import *
from copy import deepcopy

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums)<k:
            return None
        
        heap = deepcopy(nums[:k])
        #Build up the heap
        heapify(heap)
        
        for i in xrange(k, len(nums)):
            if nums[i]>heap[0]:
                heapreplace(heap, nums[i])  # pop then push
        
        return heap[0]

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        
        for num in nums:
            if num<pivot:
                nums2.append(num)
            elif num>pivot:
                nums1.append(num)
        
        if k<=len(nums1):
            return self.findKthLargest(nums1, k)
        elif k>(len(nums)-len(nums2)):
            return self.findKthLargest(nums2, k-(len(nums)-len(nums2)))
        else:
            return pivot
                