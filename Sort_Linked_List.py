# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        mid = self.findMedia(head)
        # self.printf(mid)
        
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)
        
    def findMedia(self, head):
        
        if head is None:
            return head
        
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def merge(self, headA, headB):
        # print "headA ->", printf(headA)
        # print "headB ->", printf(headB)

        nodeA = headA
        nodeB = headB
        
        dummy = ListNode(0)
        prev = dummy
        
        while nodeA and nodeB:
            if nodeA.val < nodeB.val:
                prev.next = nodeA
                nodeA = nodeA.next
            else:
                prev.next = nodeB
                nodeB = nodeB.next
            prev = prev.next
            
        if nodeA:
            prev.next = nodeA
        
        else:
            prev.next = nodeB
        
        return dummy.next
    
def printf(head):
    if head is None:
        # print None
        return None
    print_list = []
    
    while head:
        # print head.val
        print_list.append(head.val)
        head = head.next
    
    return print_list
        

array = [1,3,2,4,5]
node = None
head = None
for item in array:
    if node is None:
        node = ListNode(item)
        head = node
    else:
        node.next = ListNode(item)
        node = node.next

printf(head)

sol = Solution()
sol.sortList(head)
printf(head)