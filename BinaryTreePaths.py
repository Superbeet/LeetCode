# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        self.result = []

        if root!=None:
        	self.find_path(root, root.val)

     	return self.result

    def find_path(self, node, path):

     	if node.left==None and node.right==None:
     		self.result.append(str(path))

     	if node.left!=None:
     		self.find_path(node.left, "%s->%s" %(path, node.left.val))

     	if node.right!=None:
     		self.find_path(node.right, "%s->%s" %(path, node.right.val))




