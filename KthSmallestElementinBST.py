# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Method 1: Using Inorder Traversal.
Inorder traversal of BST retrieves elements of tree in the sorted order. 
The inorder traversal uses stack to store to be explored nodes of tree (threaded 
tree avoids stack and recursion for traversal, see this post). The idea is to 
keep track of popped elements which participate in the order statics.
"""
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root

        while node:
            stack.append(node)
            node = node.left

        x = 1

        while stack and x<=k:
            node = stack.pop(-1)
            x += 1
            right_node = node.right

            while right_node:
                stack.append(right_node)
                right_node = right_node.left

        return node.val

"""
Method 2: Augmented  Tree Data Structure.
The idea is to maintain rank of each node. We can keep track of elements in a subtree of any node while building the tree. Since we need K-th smallest element, we can maintain number of elements of left subtree in every node.
Assume that the root is having N nodes in its left subtree. If K = N + 1, root is K-th node. If K < N, we will continue our search (recursion) for the Kth smallest element in the left subtree of root. If K > N + 1, we continue our search in the right subtree for the (K – N – 1)-th smallest element. Note that we need the count of elements in left subtree only.
Time complexity: O(h) where h is height of tree.
"""
