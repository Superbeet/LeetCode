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

# Runtime: 44 ms
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = stack()
        node = root
        result = []

        while node!=None or s.size()!=0:
            
            while node!=None:
                result.append(node.val)

                s.push(node)
                node = node.left

            node = s.pop()
            node = node.right

        return result

# Runtime: 44 ms
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = stack()
        result = []

        if root == None:
            return result

        s.push(root)

        while not s.empty():
            p = s.pop()

            result.append(p.val)

            if p.right:
                s.push(p.right)

            if p.left:
                s.push(p.left)

        return result



