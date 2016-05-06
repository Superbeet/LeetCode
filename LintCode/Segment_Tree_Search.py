"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

                  [0, 3, max=4]
                 /             \
          [0,1,max=4]        [2,3,max=3]
          /         \        /         \
   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
"""

class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]

    def build(self):
        node = SegmentTreeNode(0,6,10)

        node.left = SegmentTreeNode(0,3,10)
        node.right = SegmentTreeNode(4,6,9)

        node.left.left = SegmentTreeNode(0,1,10)
        node.left.right = SegmentTreeNode(2,3,5)

        node.right.left = SegmentTreeNode(4,5,9)
        node.right.right = SegmentTreeNode(6,6,3)

        node.left.left.left = SegmentTreeNode(0,0,1)
        node.left.left.right = SegmentTreeNode(1,1,1)

        node.left.right.left = SegmentTreeNode(2,2,2)
        node.left.right.right = SegmentTreeNode(3,3,5)

        node.right.left.left = SegmentTreeNode(4,4,1)
        node.right.left.right = SegmentTreeNode(5,5,9)

        node.right.right = SegmentTreeNode(6,6,3)

        return node


    def query(self, root, start, end):
        # write your code here
        
        # print "root->start, root->end", [ root.start, root.end], "start, end", [start, end]

        if root is None:
            return -float("INF")

        if start > root.end or end < root.start or start>end:
            return -float("INF")

        if start <= root.start and end >= root.end:
            return root.max

        mid = root.start + (root.end - root.start)/2
        
        # print start, mid
        left_max = self.query(root.left, start, min(mid, end))
        # print mid, end
        right_max = self.query(root.right, max(start, mid), end)
        
        return max(left_max, right_max)

sol = Solution()
root = sol.build()
# print sol.query(root, 1, 2)
print sol.query(root, 1, 5)