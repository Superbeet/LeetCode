# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def countUnivalSubtrees(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None:
			return 0

		self.count = 0
		self.find_unival_subtrees(root)
		return self.count

	def find_unival_subtrees(self, node):

		if node==None:
			return True

		if node.left == None and node.right == None:
			self.count += 1
			return True

		left = self.find_unival_subtrees(node.left)

		right = self.find_unival_subtrees(node.right)

		if left and right and (node.left == None or node.val == node.left.val) and (node.right == None or node.val == node.right.val):
			self.count += 1
			return True
		else:
			return False
