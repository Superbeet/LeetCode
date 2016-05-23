from heapq import *

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashtable = {}
        
        size = len(nums)
        
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        elements = []
        
        for num, freq in hashtable.iteritems():
            heappush(elements, (freq, num))
        
        key_elements = nlargest(k, elements)
        
        return [num for freq, num in key_elements]


from heapq import *
class MinHeap(object):
    def __init__(self, k):
        self.k = k
        self.heap = []
    
    def push(self, rank, elem):
        if len(self.heap)<self.k:
            heappush(self.heap, (rank, elem))
        else:
            if self.heap[0][0]<rank:
                heapreplace(self.heap, (rank, elem))
    
    def items(self):
        elements = nlargest(self.k, self.heap)
        return [elem for rank, elem in elements]

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = MinHeap(k)
        
        hashtable = {}
        
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        
        for num,freq in hashtable.iteritems():
            heap.push(freq, num)
        
        return heap.items()
            
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print sol.topKFrequent(nums, k)