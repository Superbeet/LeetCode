# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return self.find_longest(root, root.val-1, 0)

    def find_longest(self, node, pre_val, pre_length):

        if node == None:
            return pre_length

        cur_length = pre_length+1 if pre_val+1==node.val else 1

        return max(cur_length, 
                    self.find_longest(node.left, node.val, cur_length), 
                        self.find_longest(node.right, node.val, cur_length))