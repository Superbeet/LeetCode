# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq		
class Solution(object):
    def minMeetingRooms(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		size = len(intervals)
		
		if intervals == None or len(intervals)==0:
		    return 0
		
		intervals = sorted(intervals, key=lambda i: (i.start, i.end))
		
		end_times = []
		heapq.heapify(end_times)
		heapq.heappush(end_times, intervals[0].end)

		for i in xrange(1, size):
			if intervals[i].start >= end_times[0]:
				heapq.heappop(end_times)

			heapq.heappush(end_times, intervals[i].end)
		
		return len(end_times)
 
sol = Solution()
L  = [[2,7]]
intervals = []
for s,e in L:
	intervals.append(Interval(s, e))

print sol.minMeetingRooms(intervals)