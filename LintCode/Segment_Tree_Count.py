"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""
class Solution: 
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        if root is None:
            return 0
        
        if start > root.end and end < root.start and start > end:
            return 0
        
        if start <= root.start and end >= root.end:
            return root.count
        
        mid = root.start + (root.end - root.start)/2
        
        left_num = self.query(root.left, start, min(mid, end))
        
        right_num = self.query(root.right, max(start, mid), end)
        
        return left_num + right_num

class Solution: 
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        node = SegmentTreeNode(start, end)
        
        # if start>end:
        #     return None
        
        if start==end:
            return node
        
        mid = (start+end)/2
        node.left = self.build(start, mid)
        node.right = self.build(mid+1, end)
        
        return node