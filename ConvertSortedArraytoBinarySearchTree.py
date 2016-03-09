# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		return self.add_node(num, 0, len(nums)-1)

	def add_node(self, num, start, end):
		if start>end:
			return None

		mid = (start+end)/2
		root = TreeNode(num[mid])
		root.left = self.add_node(num, start, mid-1)
		root.right = self.add_node(num, mid+1, end)

		return root
