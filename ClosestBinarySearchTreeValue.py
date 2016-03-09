# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None


"""
根据二叉树的性质，我们知道当遍历到某个根节点时，最近的那个节点要么是在子树里面，要么就是根节点本身。所以我们根据这个递归，返回子树中最近的节点，和根节点中更近的那个就行了。
"""
class Solution(object):
	def closestValue(self, root, target):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		if not root:
			return None
		
		cur_val = root.val
		
		child = (root.left if target<root.val else root.right)
		
		if child == None:
			return cur_val
		
		closet = self.closestValue(child, target)
		
		return (closet if abs(target-closet)<abs(target-cur_val) else cur_val)