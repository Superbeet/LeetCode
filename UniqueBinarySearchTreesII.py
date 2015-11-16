# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
     	return self.genBST(1, n)

    def genBST(self, min, max):
    	res = []

    	if min>max:
    		res.append(None)
    		return res

    	for i in range(min, max+1):
    		left_subtree = self.genBST(min, i-1)
    		right_subtree = self.genBST(i+1, max)

    		for j in range(0, len(left_subtree)):
    			for m in range(0, len(right_subtree)):
    				
    				node = TreeNode(i)
    				node.left = left_subtree[j]
    				node.right = right_subtree[m]
    				res.append(node)

    	return res