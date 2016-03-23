# -*- coding: utf-8 -*-
"""
2. 给定一个binary tree，判断他是否既是valid BST又是balanced。follow up是如果要hack这个function让它出错，应该怎么输入，还有如果输入是极端情况会有什么影响如何优化，比如全是右子数或者million of nodes.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def is_valid_balanced_BST(self, root):
		return self.check_valid_balanced_BST(root, -float("INF"), float("INF"))

	def check_valid_balanced_BST(self, node, min_val, max_val):
		if node == None:
			return 0

		if node.val<=min_val or node.val>=max_val:
			return -1
			
		left = self.check_valid_balanced_BST(node.left, min_val, node.val)
		right = self.check_valid_balanced_BST(node.right, node.val, max_val)

		if left<0 or right<0 or abs(left-right)>1:
			return -1
		# print "left->%s, right->%s" %(left, right)
		return max(left, right)+1

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
print sol.is_valid_balanced_BST(root)