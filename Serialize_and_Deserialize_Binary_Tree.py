# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Pre-order traversal
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def do_serialize(node):

            if node is None:
                serial.append('#')
                return

            serial.append(str(node.val))
            do_serialize(node.left)
            do_serialize(node.right) 
            
        serial = []

        if not root:
            return None

        do_serialize(root)

        return serial

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def do_deserialize(data, index):

            if index[0]>=len(data) or data[index[0]]=='#':
                return None

            node = TreeNode(int(data[index[0]]))
            index[0] += 1
            node.left = do_deserialize(data, index)
            index[0] += 1
            node.right = do_deserialize(data, index)

            return node

        if not data:
            return None

        index = [0]

        return do_deserialize(data, index)

# """
# Level-order traversal
# """
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        serial = []
        queue = []

        if not root:
            return serial

        node = root
        queue.append(node)

        while node or len(queue):

            node = queue.pop(0)

            if node is None:
                serial.append('#')

            else:
                serial.append(node.val)

                queue.append(node.left)

                queue.append(node.right)

        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        # serial = eval(data)

        def deserial(sub_serial, pre_level_nodes):
            
            # print sub_serial

            if not sub_serial or not pre_level_nodes:
                return 

            i = 0
            size = len(pre_level_nodes)
            level_nodes = []

            while i<size:

                if sub_serial[2*i] == '#':
                    pre_level_nodes[i].left = None
                else:
                    pre_level_nodes[i].left = TreeNode(sub_serial[2*i])

                    level_nodes.append(pre_level_nodes[i].left)

                if sub_serial[2*i+1] == '#':
                    pre_level_nodes[i].right = None
                else:
                    pre_level_nodes[i].right = TreeNode(sub_serial[2*i+1])

                    level_nodes.append(pre_level_nodes[i].right)

                i += 1

            deserial(sub_serial[2*i:], level_nodes)

        root = TreeNode(data[0])
        deserial(data[1:], [root])
        return root


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    result = []

    if not root:
        return result

    queue = []
    queue.append((root,0))  
    
    while len(queue)!=0:

        node, level = queue.pop(0)

        if level == len(result):
            result.append([])

        result[level].append(node.val)

        if node.left:
            queue.append((node.left, level+1))
        
        if node.right:
            queue.append((node.right, level+1))

    return result



# Your Codec object will be instantiated and called as such:

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

# root = TreeNode(6)
# root.left = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(4)
# root.right = TreeNode(8)
# root.right.right = TreeNode(10)
# root.right.right.right = TreeNode(12)

codec = Codec()
print levelOrder(root)
serial = codec.serialize(root)
print serial
root = codec.deserialize(serial)
print levelOrder(root)
# print root.left.left

# codec.deserialize(codec.serialize(root))