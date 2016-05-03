import collections

class Iterator(object):
    def __init__(self, vals):
        self.v = vals
        self.i = -1
    
    def next(self):
        self.i += 1
        return self.v[self.i]
    
    def has_next(self):
        return self.i+1<len(self.v)

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        iter_1 = Iterator(v1)
        iter_2 = Iterator(v2)
        self.queue = collections.deque([])
        if iter_1.has_next():
            self.queue.append(iter_1)
        if iter_2.has_next():
            self.queue.append(iter_2)
        
    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return 
        it = self.queue.popleft()
        res = it.next()
        if it.has_next():
            self.queue.append(it)
        return res
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue)>0
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())