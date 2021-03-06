# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""

		result = []

		if not root:
			return result

		queue = []
		queue.append((root,0))  
		
		while len(queue)!=0:

			node, level = queue.pop(0)

			if level == len(result):
				result.append([])

			result[level].append(node.val)

			if node.left:
				queue.append((node.left, level+1))
			
			if node.right:
				queue.append((node.right, level+1))

		return result


