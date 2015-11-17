# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        all_nodes = []
        self.preorder(root, all_nodes)
        n = len(all_nodes)

        for i in range(0, n-1):
            all_nodes[i].left = None
            all_nodes[i].right = all_nodes[i+1]

        all_nodes[n-1].left  = None
        all_nodes[n-1].right = None


    def preorder(self, node, all_nodes):
        if not node:
            return
        all_nodes.append(node)
        self.preorder(node.left, all_nodes)
        self.preorder(node.right, all_nodes)

"""
Why right_tail firstly? No idea
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def flattenBT(node):
            if not node:
                return None
            left_tail = flattenBT(node.left)
            right_tail = flattenBT(node.right)
            
            if node.left:
                temp = node.right
                node.right = node.left
                node.left = None
                left_tail.right = temp

            if right_tail:
                return right_tail

            if left_tail:
                return left_tail

            return node

        flattenBT(root)

"""
real-time inorder transformation
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        last_visited_node = [None]

        def flattenBT(node):
            if node is None:
                return
            # right_node = node.right
            if last_visited_node[0] is not None:
                last_visited_node[0].left = None
                last_visited_node[0].right = node

            last_visited_node[0] = node

            flattenBT(node.left)
            flattenBT(node.right)

        flattenBT(root)

root = TreeNode(1)
root.left = TreeNode(2)

sol = Solution()
sol.flatten(root)