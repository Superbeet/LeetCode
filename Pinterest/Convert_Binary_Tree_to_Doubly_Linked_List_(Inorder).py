"""
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

                                            10
                                          /    \
                                        6       14
                                      /  \     /　 \
                                   4     8  12   16
                                   
This is the recursive approach. Note that, here root will point to some inbetween element of the list formed. So,just traverse from root backwards to get the head.

"""

import copy

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convert_node(node, is_left = None):
    
    if node is None:
        return node

    node.left = convert_node(node.left, True)
    
    if node.left is not None:
        node.left.right = node
        # node.left = node.left
        
    node.right = convert_node(node.right, False)
    
    if node.right is not None:
        # node.right = node.right
        node.right.left = node
    
    curr = node
    # if the current node is the right child of its parent
    # return the least node 
    if is_left:
        while curr.right is not None:
            curr = curr.right
    else:
        while curr.left is not None:
            curr = curr.left
    
    return curr

def print_list(node):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.right
    print result


def binary_tree_to_list(root):
    convert_node(root)
    while root.left is not None:
        root = root.left
    
    print_list(root)

# Test
root = TreeNode(10)
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right = TreeNode(14)
# root.right.left = TreeNode(12)
root.right.right = TreeNode(16)

node = binary_tree_to_list(root)
# print_list(node)