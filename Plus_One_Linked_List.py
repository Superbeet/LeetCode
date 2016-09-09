# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        carry = 1
        head = self.reverse(head)
        
        prev = None
        curr = head
        while curr:
            prev = curr
            
            digit = (curr.val + carry)%10
            carry = (curr.val + carry)/10
            
            curr.val = digit
            curr = curr.next            
        
        if carry != 0:
            prev.next = ListNode(carry)
        
        return self.reverse(head)
        
    def reverse(self, head):
        if head is None:
            return None
        
        dummy = ListNode(-1)
        curr = head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next
    
    def printf(self, head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        
        print "->".join(result)
    