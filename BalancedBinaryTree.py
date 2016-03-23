# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return False if self.find_depth(root)==-1 else True
		
	def find_depth(self, root):
		if not root:
			return 0
		
		left_depth = self.find_depth(root.left)
		if left_depth == -1:
			return -1
		
		right_depth = self.find_depth(root.right)
		
		if right_depth == -1:
			return -1
		
		if abs(left_depth-right_depth)>1:
			return -1
		
		return max(left_depth, right_depth)+1