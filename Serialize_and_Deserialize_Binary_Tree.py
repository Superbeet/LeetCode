# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

            node = queue.pop()

            if node is None:
                serial.append(None)
            else:
                serial.append(node.val)

                queue.append(node.left)

                queue.append(node.right)

        return str(serial)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        # serial = eval(data)
        root = TreeNode(serial[0])

        def deserial(sub_serial, pre_level_nodes):
            
            if not sub_serial or not pre_level_nodes:
                return 

            i = 0
            size = len(pre_level_nodes)
            level_nodes = []

            # print sub_serial
            
            while i<size:

                # print i

                pre_level_nodes[i].left = TreeNode(sub_serial[2*i])

                pre_level_nodes[i].right = TreeNode(sub_serial[2*i+1])

                level_nodes.append(pre_level_nodes[i].left)

                level_nodes.append(pre_level_nodes[i].right)

                i += 1

            deserial(sub_serial[2*i:], level_nodes)

        deserial(serial[1:], [root])
        return root


# Your Codec object will be instantiated and called as such:

root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(8)
root.right.right = TreeNode(10)
root.right.right.right = TreeNode(12)

codec = Codec()
# serial = codec.serialize(root)
# print serial
# print codec.deserialize(serial)

codec.deserialize(codec.serialize(root))