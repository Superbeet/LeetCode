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

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        s = stack()
        result = []

        node = root

        if node == None:
            return result

        while not s.empty() or node!=None:

            while node!=None:

                s.push(node)

                node = node.left

            node = s.pop()

            result.append(node.val)

            node = node.right

        return result




        