# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def printIntervals(intervals):
	for int in intervals:
		print (int.start, int.end)
		
		
class Solution(object):
	def canAttendMeetings(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: bool
		"""
		size = len(intervals)
		
		if intervals == None or len(intervals)==0:
		    return True
		
		intervals = sorted(intervals, key=lambda i: (i.start, i.end))
		
		for i in xrange(0, size-1):
			if not self.overlap(intervals[i], intervals[i+1]):
				return False
		return True

	def overlap(self, interval1, interval2):
		return interval1.end <= interval2.start

intervals = []
obj = Interval(13,15)
obj_2 = Interval(1,13)
intervals.append(obj)
intervals.append(obj_2)
# print len(intervals)
sol = Solution()
print sol.canAttendMeetings(intervals)