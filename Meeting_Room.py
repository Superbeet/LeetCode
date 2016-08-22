# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
            
        intervals.sort(key = lambda x:(x.start, x.end))
        
        prev = intervals[0]
        for i in xrange(1, len(intervals)):
            curr = intervals[i]
            if prev.end > curr.start:
                return False
            prev = curr
            
        return True


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        edge_list = []
        for interval in intervals:
            edge_list.append((interval.start, True))
            edge_list.append((interval.end, False))
        edge_list.sort()
        count = 0
        max_count = 0
        for edge, is_start in edge_list:
            if is_start:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
        
        return max_count        
        
from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:(x.start, x.end))

        
        heap = []
        heappush(heap, intervals[0].end)
        
        for interval in intervals[1:]:
            if interval.start >= heap[0]:
                heapreplace(heap, interval.end)
            else:
                heappush(heap, interval.end)
        
        return len(heap)
        
        
        