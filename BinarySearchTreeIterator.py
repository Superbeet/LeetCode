# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time O(1) Space O(n)
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_left(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0

    def next(self):
        """
        :rtype: int
        """
        # node itself
        top = self.stack.pop()
        # right smallest node
        self.push_left(top.right)
        return top.val

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Time O(1) Space O(tree_size)
class BSTIterator(object):
    def __init__(self, root):
        self.tree = []
        self.in_order_traverse(root)
        self.idx = -1
        self.size = len(self.tree)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx+1<self.size

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.tree[self.idx]

    def in_order_traverse(self, node):

        if node is None:
            return

        self.in_order_traverse(node.left)
        
        self.tree.append(node.val)

        self.in_order_traverse(node.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())