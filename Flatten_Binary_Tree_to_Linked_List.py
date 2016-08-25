# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Divide and Conquer

    1
  /    \
 2     5
  \       \
   3      6 <- rightTail
     \
      4  <- leftTail

1 - 2 - 3 - 4 - 5 - 6

Pre-order

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
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root)
        
    def flatten_helper(self, root):
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        if root.left is None:
            return self.flatten_helper(root.right)
        
        if root.right is None:
            root.right = root.left
            root.left = None
            return self.flatten_helper(root.right)
        
        left_tail = self.flatten_helper(root.left)
        right_tail = self.flatten_helper(root.right)
        
        left_tail.right = root.right
        root.right = root.left
        root.left = None
        return right_tail

"""
off-line preorder transformation with extra space
"""
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
real-time preorder transformation
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        def flattenBT(node, last_visited_node):
            if node is None:
                return
            # store the orginal right child
            right_node = node.right

            # modify the right child and set the left child to None
            if last_visited_node[0] is not None:
                last_visited_node[0].right = node
                last_visited_node[0].left = None

            # update last_visited_node
            last_visited_node[0] = node

            flattenBT(node.left, last_visited_node)
            flattenBT(right_node, last_visited_node)

        flattenBT(root, [None])

""" 
root's right subtree's predecessor is the rightmost node of its left child  
"""
class Solution:
    def flatten(self, root):
        # eliminate each level's root's left child
        while root:
            if root.left:
                p = root.left

                while p.right: 
                    p = p.right

                p.right = root.right
                root.right = root.left
                root.left = None

            root = root.right

"""
real-time inorder transformation
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def do_flatten(self, node):
            if node is None:
                return None

            right_child = root.right
            new_head = node

            left_tree = do_flatten(node.left)

            if left_tree:   #left_tree!=None
                new_head = left_tree
                tail = left_tree.left
                tail.right = node
                node.left = tail
                left_tree.left = root

            right_tree = do_flatten(right_child)

            if right_tree:
                root.right = right_tree
                new_head.left = right_tree.left
                right_tree.left = root

            return new_head



class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """



root = TreeNode(1)
root.left = TreeNode(2)

sol = Solution()
sol.flatten(root)