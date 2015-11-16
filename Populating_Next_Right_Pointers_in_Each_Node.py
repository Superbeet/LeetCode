# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return None

        queue = []
        queue.append(root)
        queue.append(None)    # None for level mark

        pre = None

        while queue:

            node = queue.pop(0)

            if node is not None:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            elif queue:	
                queue.append(None)

            if pre!=None:
                pre.next = node

            pre = node







root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
# root.left.left = TreeLinkNode(4)
# root.left.right = TreeLinkNode(5)
# root.right.left = TreeLinkNode(6)
# root.right.right = TreeLinkNode(7)

sol = Solution()
sol.connect(root)







            # for i in range(0, len(self.queue)):

            #     if i%2==0:
            #         if self.queue[i].right != None:
            #             self.queue[i].left.next = self.queue[i].right
            #         else:
            #             self.queue[i].left.next = None
            #     else:
            #         if self.queue[i+1].left != None:
            #             self.queue[i].right.next = self.queue[i+1].left
            #         else:
            #             self.queue[i].right.next = None

