# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []

        if root==None:
        	return res

        queue = [root]

        while queue:
            
            size = len(queue)

            for i in range(size):

                node = queue.pop(0)

                if i == 0:
                    res.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return res


