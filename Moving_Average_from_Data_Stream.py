from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque([])
        self.cur_sum = 0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        cur_sum = 0
        
        if len(self.queue) < self.size:
            self.cur_sum += val
        else:
            last_num = self.queue.popleft()
            self.cur_sum = self.cur_sum - last_num + val
        self.queue.append(val)
        
        return self.cur_sum/float(len(self.queue))