# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxint

minint = -maxint - 2

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = [minint]

        def find_max_sum(node, max_sum):
            if not node:
                return 0

            path_sum_left = 0
            path_sum_right = 0

            if root.left:
                # negative val should not be passed
                path_sum_left = max(find_max_sum(node.left, max_sum), 0)

            if root.right:
                path_sum_right = max(find_max_sum(node.right, max_sum), 0)

            ps1_node = max(path_sum_left, path_sum_right) + node.val
            ps2_node = path_sum_left + path_sum_right + node.val

            max_sum[0] = max(max_sum[0], max(ps1_node, ps2_node))

            return ps1_node

        find_max_sum(root, max_sum)

        return max_sum[0]