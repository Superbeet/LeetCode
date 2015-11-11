# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)!=len(inorder):
        	return None

        if len(preorder)==0:
        	return None

        if len(preorder)==1:
        	return TreeNode(preorder[0])

        self.do_build_tree(preorder, inorder, 
        					0, len(preorder)-1, 0, len(inorder)-1)

    def do_build_tree(self, preorder, s1, e1, inorder, s2, e2):

    	if s1>e1 or s2>e2:
    		return None

    	root_val = preorder[s1]

    	print "s1->%s , root_val->%s" %(s1, root_val)

    	root = TreeNode(root_val)

    	rootIndex = -1

    	for i in xrange(0, e2+1):
    		if inorder[i]==root_val:
    			rootIndex = i
    			break

    	# if rootIndex == -1:
    	# 	return None

    	length = rootIndex-s2

    	root.left  = self.do_build_tree(preorder, s1+1, s1+length, inorder, s2, rootIndex-1)

    	root.right = self.do_build_tree(preorder, s1+length+1, e1, inorder, rootIndex+1, e2)

    	return root
