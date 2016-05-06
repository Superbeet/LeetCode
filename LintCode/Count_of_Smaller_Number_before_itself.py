# http://www.jianshu.com/p/a2aae061d637

class segmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None

class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def build_segment_tree(self, start, end):
        root = SegmentTreeNode(start, end, 0)
        
        if start > end:
            return None
            
        if start == end:
            return root
            
        mid = (start + end)/2
        root.left = self.build_segment_tree(start, mid)
        root.right = self.build_segment_tree(mid+1, end)
        return root
    
    def query_segment_tree(self, root, start, end):
        if root is None:
            return 0
        
        if start>root.end or end<root.start or start>end:
            return 0
            
        if root.start==start and root.end==end:
            return root.count

        mid = (root.start + root.end)/2
        left_count = self.query_segment_tree(root.left, start, min(mid,end))
        right_count = self.query_segment_tree(root.right, max(start,mid+1), end)

        return left_count + right_count
    
    def modify_segment_tree(self, root, num, value):
        if root.start == num and root.end == num:
            root.count += value
            return

        mid = (root.end + root.start) / 2
        
        if root.start <= num and num <= mid:
            self.modify_segment_tree(root.left, num, value)

        if mid < num and num <= root.end:
            self.modify_segment_tree(root.right, num, value)

        root.count = root.left.count + root.right.count

    def countOfSmallerNumberII(self, A):
        root = self.build_segment_tree(0, 10000)

        result = []
        for num in A:
            count = 0
            if num>0:
                count = self.query_segment_tree(root, 0, num - 1)
            self.modify_segment_tree(root, num, 1)
            result.append(count)
            
        return result