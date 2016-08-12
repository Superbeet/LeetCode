# Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        
        self.current = head
        size = self.get_length(head)
        
        return self.build_bst(size)
    
    def get_length(self, head):
        
        if head is None:
            return 0
            
        length = 0
        
        while head:
            length += 1
            head = head.next
        
        return length
    
    # preorder traverse
    def build_bst(self, size):
        if self.current is None or size<=0:
            return None
        
        mid = size/2
        left = self.build_bst(mid)
        parent = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.build_bst(size-mid-1)
        
        parent.left = left
        parent.right = right
        
        return parent
        