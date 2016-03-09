# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#方法一: use range to do jungement, need integer boundary
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_valid_BST(root, -sys.maxint-1, sys.maxint)

    def check_valid_BST(self, node, min, max):

        if node == None:
            return True

        if node.val<=min or node.val>=max:
            return False

        return self.check_valid_BST(node.left, min, node.val) and \
                self.check_valid_BST(node.right, node.val, max)


class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = -sys.maxint-1
        return self.check_valid_BST(root)

    def check_valid_BST(self, node):

        if node == None:
            return True

        if self.check_valid_BST(node.left)==False:
            return False

        if node.val<=prev:
            return False

        self.prev = node.val

        if self.check_valid_BST(node.right)==False:
            return False

        return True





root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sol = Solution()
print sol.isValidBST(root)