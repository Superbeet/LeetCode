# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionIterative(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
        	return None

        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        
        return root

class SolutionRecursive(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = []

        while root:
        	node = queue.pop(0)
        	tmp = node.left
        	node.right = node.left
        	node.left = tmp

        	if node.left:
        		queue.append(node.left)

        	if node.right:
        		queue.append(node.right)

        return root

