# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.count_node(root, 0, 0)

	def count_node(self, node, l_height, r_height):
		
		if l_height == -1:
			l_height = 0
			curr = node
			while curr!=None:
				l_height+=1
				curr = curr.left

		if r_height == -1:
			r_height = 0
			curr = node
			while curr!=None:
				r_height+=1
				curr = curr.right

		if l_height == r_height:
			return 1<<l_height - 1

		return self.count_node(node.left, l_height-1, -1) + \
				self.count_node(node.right, -1, r_height-1) + 1
