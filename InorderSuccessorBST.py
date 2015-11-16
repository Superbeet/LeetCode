# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
There are just two cases:
The easier one: p has right subtree, then its successor is just the leftmost child of its right subtree;
The harder one: p has no right subtree, then a traversal is needed to find its successor.
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right!=None:
            return self.left_most_node(root.right)

        suc = None

        while root:

            if p.val<root.val:
                suc = root
                root = root.left

            elif p.val>root.val:
                root = root.right

            else:
                break

        return suc

    def left_most_node(self, node):
        while node.left:
            node = node.left
        return node