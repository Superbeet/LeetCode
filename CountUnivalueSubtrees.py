# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0

        res = self.find_unival_subtree(root, None)
        
        return res[0]

    def find_unival_subtree(self, node, last_val):

        if node == None:
            return (0, True)

        if node.left == None and node.right == None:
            return (1, True)

        left_count, left_flag  = self.find_unival_subtree(node.left, node.val)

        right_count, right_flag = self.find_unival_subtree(node.right, node.val)

        print "left_count, right_count -> %s,%s" %(left_count, right_count)
        
        if left_flag and right_flag and last_val==node.val:
            return (left_count+right_count+1, True)
        
        else:
            return (left_count+right_count, False)
