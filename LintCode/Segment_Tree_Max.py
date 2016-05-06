"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""

class Solution: 
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]

    def build(self, A):
        # write your code here
        return self.build_tree(0, len(A)-1, A)
        
    def build_tree(self, start, end, array):
        if start>end:
            return None
        
        root = SegmentTreeNode(start, end, -float("INF"))
        
        if start!=end:
            mid = (start + end)/2
            root.left = self.build_tree(start, mid, array)
            root.right = self.build_tree(mid+1, end, array)
            root.max = max(root.left.max, root.right.max)
        
        else:
            root.max = array[start]
        
        return root

    def query(self, root, start, end):
        # write your code here
        if root is None:
            return -float("INF")

        if start > root.end or end < root.start or start>end:
            return -float("INF")

        if start == root.start and end == root.end:
            return root.max

        mid = root.start + (root.end - root.start)/2
        
        # print start, mid
        left_max = self.query(root.left, start, min(mid, end))
        # print mid, end
        right_max = self.query(root.right, max(start, mid), end)
        
        return max(left_max, right_max)

    def modify(self, root, index, value):
        # write your code here
        
        if root is None:
            return
        
        if index>root.end or index<root.start:
            return
        
        if root.start == index and root.end == index:
            root.max = value
            return
        
        mid = (root.start + root.end)/2
        
        self.modify(root.left, index, value)
        
        self.modify(root.right, index, value)
        
        root.max = max(root.left.max, root.right.max)

        