"""
Path Sum II [Medium]

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
			  5
			 / \
			4   8
		   /   / \
		  11  13  4
		 /  \	/ \
		7	2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		self.result = []

		self.getPathSum(root, sum, 0, [])

		return self.result

	def getPathSum(self, node, target_sum, cur_sum, cur_path):

		if node == None:
			return 

		if node.left == None and node.right == None:
			if cur_sum + node.val == target_sum:
				self.result.append(cur_path + [node.val])
			return

		self.getPathSum(node.left, target_sum, cur_sum+node.val, cur_path+[node.val])

		self.getPathSum(node.right, target_sum, cur_sum+node.val, cur_path+[node.val])

		return