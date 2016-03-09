# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.check_symmetry(root, root)
		
	def check_symmetry(self, node1, node2):

		# None node needs to be considered seperately, because they don't have values
		if node1 == None and node2 == None:
			return True

		if (node1 != None and node2 == None) or (node1 == None and node2 != None):
			return False

		# if node1 = node2 = root
		if node1 == node2:
			return self.check_symmetry(node1.left, node2.right)
			
		if node1.val != node2.val:
			return False

		return self.check_symmetry(node1.left, node2.right) and self.check_symmetry(node1.right, node2.left)

