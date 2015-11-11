# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.queue = []
        self.result = []
        level = 0
        self.queue.append((root, level))

        if root == None:
        	return self.result

        while len(self.queue):

        	node, level = self.queue.pop(0)

        	if level == len(self.result):
        		self.result.append([])

        	if level%2==1:
        		self.result[level].insert(0, node.val)
        	else:
        		self.result[level].append(node.val)

        	if node.left!=None:
        		self.queue.append((node.left,level+1))

        	if node.right!=None:
        		self.queue.append((node.right,level+1))

        return self.result

node = TreeNode(1)
sol = Solution()
print sol.zigzagLevelOrder(node)