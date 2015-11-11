# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_valid_BST(root, None, None)

    def check_valid_BST(self, node, min_val, max_val):

        if node == None:
            return True

        if min_val == None:
            min_val = node.val
        else:
            min_val = min(min_val, node.val)
            
        if max_val == None:
            max_val = node.val
        else:
            max_val = max(max_val, node.val)
            
        # equal is also False

        if (node.left==None or node.left.val<min_val) and (node.right==None or node.right.val>max_val):
            return True

        # if node.right.val>max_val or node.right==None:
        #     return True

        # left_flag = self.check_valid_BST(node.left, min_val, max_val)

        # right_flag = self.check_valid_BST(node.right, min_val, max_val)

        return self.check_valid_BST(node.left, min_val, max_val) and self.check_valid_BST(node.right, min_val, max_val)

root = TreeNode(1)
root.left = TreeNode(1)

sol = Solution()
print sol.isValidBST(root)