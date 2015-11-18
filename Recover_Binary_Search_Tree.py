# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

"""
O(n) space
"""
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return None

        def inorder_check(node, elem):
            """
            elem = [s1, s2, pre]
            """
            if node is None:
                return

            inorder_check(node.left, elem)

            if node is not None and elem[2] is not None and node.val<elem[2].val:
                if elem[0] is None:
                    elem[0] = elem[2] # s1=pre
                    elem[1] = node    # s2=node
                else:
                    elem[1] = node
            
            elem[2] = node

            inorder_check(node.right, elem)

        element = [None, None, None]

        inorder_check(root, element)

        element[0].val,element[1].val = element[1].val,element[0].val

root = TreeNode(0)
root.left = TreeNode(1)

sol = Solution()
sol.recoverTree(root)