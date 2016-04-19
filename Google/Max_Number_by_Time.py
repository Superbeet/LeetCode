from heapq import *

class Votes():
    def __init__(self, votes):
        self.candi_count = {}
        for candi, time in votes:
            if time<current:
                if candi_count not in self.candi_count:
                    self.candi_count[candi] = 1
                else:
                    self.candi_count[candi] += 1

        self.heap = []
        for candi,count in self.candi_count.iteritems():
            heappush(self.heap, (-count, candi))

    def get_max_number(self, current):
        max_candi = ""
        max_count = -float("INF")
        for candi,count in self.candi_count.iteritems():
            if count>max_count:
                max_count = count
                max_candi = candi

        return max_candi

    def get_max_k_numbers(self, current, k):
        res = []
        for i in xrange(0, k):
            res.append(heappop(self.heap))

        return res

