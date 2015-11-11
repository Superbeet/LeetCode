"""Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
		1
	   / \
	  2   3
	 / \
	4   5
   / \
  6   7
return the root of the binary tree [4,5,2,#,#,3,1].

  6
 / \
7   4  
   / \
  5   2
	 / \
	3   1
"""

class Solution(object):
	def upsideDownBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root is None:
			return None
			
		new = self.build_upside_down(root)
		return new

	def build_upside_down(self, node):
		if node.left is None:
			return node

		new_root = self.build_upside_down(root.left)
		new_node.left = node.right
		new_node.right = node

		return new_node.right
