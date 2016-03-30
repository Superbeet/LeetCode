# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time - Heap - O(nklog(k)
import heapq
class MinHeap(object):
	def __init__(self, k=None):
		if k==None:
		    self.k = float("INF")
		else:
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
	
	def is_empty(self):
		return len(self.data)==0
	
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists)==0:
            return []
            
        heap = MinHeap()
        res = []
        
        for node in lists:
            while node: 
                heap.push(node.val)
                node = node.next
        
        while not heap.is_empty():
            res.append(heap.pop())
        
        return res

# Time - Heap - O(nklog(k) - Slower than Heap
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists)==0:
            return []
        pq = PriorityQueue()
        res = []
        for node in lists:
            if node:
                pq.put((node.val, node))
        
        while not pq.empty():
        	node = pq.get()[1]
        	res.append(node.val)
        	node = node.next
        	if node:
        		pq.put((node.val, node))
        		
        return res
		
sol = Solution1()
lists = [[1,2]]
size = len(lists)
root = [None for i in range(size)]
node = None
for i in range(size):
	root[i] = ListNode(lists[i][0])
	for val in lists[i]:
		if node == None:
			node = root[i]
		else:
			node.next = ListNode(val)
		node = node.next
	
print sol.mergeKLists(root)