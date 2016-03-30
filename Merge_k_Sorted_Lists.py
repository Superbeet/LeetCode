# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

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
        
        head = ListNode(0)
        head0 = head
        
        for node in lists:
            if node: 
                heap.push((node.val, node))
        
        while not heap.is_empty():
            node = heap.pop()[1]
            head.next = node
            head = head.next
            node = node.next
            if node:
            	heap.push((node.val, node))
        # Return the first node instead of head node
        return head0.next

# Time - PriorityQueue - O(nklog(k) - Slower than Heapq
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

# Binary Merge - Time - O(nklog(k)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists)==0:
            return []
        
        size = len(lists)
        end = size - 1
        while end>0:
        	start = 0
        	while start<end:
        		lists[start]=self.merge_two_lists(lists[start],lists[end])
        		start += 1
        		end -= 1
        
        return lists[0]
    
    def merge_two_lists(self, head1, head2):
        head = ListNode(0)
        node = head
        
        while head1 and head2:
        	if head1.val<=head2.val:
        		node.next = head1
        		head1 = head1.next
        	else:
        		node.next = head2
        		head2 = head2.next
        	node = node.next
        
        if head1:
        	node.next = head1
        else:
        	node.next = head2
        
        return head.next

		
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