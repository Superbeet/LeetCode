# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def peek(self):
        return self.stack[-1] 

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack)==0

# 双栈法 Post = Pre(left<->right).reverse()
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        post_path = self.postIteration(root)
        return post_path[::-1]
        
    def postIteration(self, node):

        result = []
        
        if not node:
            return result
      
        s = stack()
    
        s.push(node)

        while not s.empty():

        	node = s.pop()
        	
        	result.append(node.val)

        	if node.left:
        		s.push(node.left)

        	if node.right:
        		s.push(node.right)

        return result
