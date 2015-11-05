"""
Serialization is to store tree in a file so that it can be later restored. The structure of tree must be maintained. Deserialization is reading tree back from file.

Following are some simpler versions of the problem:

If given Tree is Binary Search Tree?
If the given Binary Tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal. In case of Binary Search Trees, only preorder or postorder traversal is sufficient to store structure information.

If given Binary Tree is Complete Tree?
A Binary Tree is complete if all levels are completely filled except possibly the last level and all nodes of last level are as left as possible (Binary Heaps are complete Binary Tree). For a complete Binary Tree, level order traversal is sufficient to store the tree. We know that the first node is root, next two nodes are nodes of next level, next four nodes are nodes of 2nd level and so on.

If given Binary Tree is Full Tree?
A full Binary is a Binary Tree where every node has either 0 or 2 children. It is easy to serialize such trees as every internal node has 2 children. We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.

How to store a general Binary Tree?
A simple solution is to store both Inorder and Preorder traversals. This solution requires space twice the size of Binary Tree.
We can save space by storing Preorder traversal and a marker for NULL pointers.
"""

import copy

class Node():
	def __init__(self, value = None):
		self.val = value
		self.left = None
		self.right = None

def serialize(root):
	str_list = []
	do_serialize(root, str_list)
	string = " ".join(str_list)
	return string

def do_serialize(root, str_list):	# tree -> string
	if root == None:
		str_list.append("/")
		return
	# string = string + " " + str(root.val)
	str_list.append(str(root.val))
	do_serialize(root.left , str_list)
	do_serialize(root.right, str_list)

def deserialize(string):	
	str_list = string.split(" ")
	# print "str_list -> ", str_list
	root = do_deserialize(str_list)
	return root

def do_deserialize(str_list):
	# print "str_list -> %s" %(str_list)
	if str_list[0] == "/":
		return None
	node = Node(str_list[0])
	# print "node->val: %s" %(node.val)

	del str_list[0]
	node.left  = do_deserialize(str_list)

	del str_list[0]
	node.right = do_deserialize(str_list)

	return node

# def do_deserialize(str_list):
# 	tmp_list = copy.copy(str_list)
# 	if tmp_list[0] == "/":
# 		return None
# 	node = Node(tmp_list[0])
# 	print "node->val: %s" %(node.val)
# 	root.left  = do_deserialize(tmp_list[1:])
# 	root.right = do_deserialize(tmp_list[1:])
# 	return node

def inorder(root):
	if root != None:
		inorder(root.left)
		if root.val != None:
			print "%s" %(root.val)
		inorder(root.right)

if __name__ == '__main__':
	root        		  = Node(20)
	root.left             = Node(8)
	root.right            = Node(22)
	root.left.left        = Node(4)
	root.left.right       = Node(12)
	root.left.right.left  = Node(10)
	root.left.right.right = Node(14)

	inorder(root)

	tmp_string = serialize(root)

	# print "tmp_string -> %s" %(tmp_string)
	
	# tmp_list = tmp_string.split(" ")
	# print "tmp_list -> %s" %(tmp_list)
	
	new_root = deserialize(tmp_string)

	# print "Inorder Traversal of the tree constructed from file:\n"
	inorder(new_root)

	
	
	