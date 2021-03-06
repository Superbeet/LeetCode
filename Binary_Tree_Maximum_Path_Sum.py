# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from sys import maxint

minint = -maxint - 2

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = [minint]
        self.find_max_sum(root, max_sum)
        return max_sum[0]

    def find_max_sum(self, node, max_sum):
        if node == None:
            return 0

        path_sum_left = 0
        path_sum_right = 0

        if node.left:
            print "root.left->", node.left.val
            # negative val should not be passed
            path_sum_left = max(self.find_max_sum(node.left, max_sum), 0)

        if node.right:
            print "root.right->", node.right.val
            path_sum_right = max(self.find_max_sum(node.right, max_sum), 0)

        # print path_sum_left, " ", path_sum_right

        ps1 = max(path_sum_left, path_sum_right) + node.val
        ps2 =     path_sum_left + path_sum_right + node.val

        # print max_sum[0]
        # print ps1, " ", ps2

        max_sum[0] = max(max_sum[0], max(ps1, ps2))

        return ps1


root = TreeNode(-6)
root.left = None
root.right = TreeNode(3)
root.right.left = TreeNode(2)

sol = Solution()
print sol.maxPathSum(root)