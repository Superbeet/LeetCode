# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		return self.is_same(p, q)

	def is_same(self, node1, node2):

		if node1 == node2:
			return True

		if node1 == None and node2 == None:
			return True

		if (node1 == None and node2 != None 
				or node1 != None and node2 == None):
			return False

		if node1.val != node2.val:
			return False

		return (self.is_same(node1.left, node2.left)
				and self.is_same(node1.right, node2.right))
