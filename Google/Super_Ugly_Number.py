# Ugly Number I
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        
        primes = [2, 3, 5]
        
        for prime in primes:
            while num>0 and num%prime==0:
                num/=prime
        
        return num==1

# Ugly Number II
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
            
        # primes = [2, 3, 5]
        index_2, index_3, index_5 = 0, 0, 0
        dp = [0 for i in range(n)]
        
        dp[0] = 1
        
        for i in xrange(1, n):
            dp[i] = min(dp[index_2]*2, dp[index_3]*3, dp[index_5]*5)
            # dp[index[j]]*j can be same, check all combinations
            if dp[i] == dp[index_2]*2:
                index_2 += 1

            if dp[i] == dp[index_3]*3:
                index_3 += 1

            if dp[i] == dp[index_5]*5:
                index_5 += 1

        return dp[n-1]

# sol = Solution()
# print sol.nthUglyNumber(1)
# print sol.nthUglyNumber(7)

# Ugly Number III
from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        size = len(primes)

        heap = []
        heapify(heap)
        heappush(heap, 1)

        for i in xrange(1, n):

            tmp = heappop(heap)
            while len(heap) and heap[0]==tmp:
                tmp = heappop(heap)

            for j in xrange(0, size):
                heappush(heap, tmp*primes[j])

        return heap[0]

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n < 1:
            return 0

        size = len(primes)
        # index array to track latest positions of primes
        index = [0 for i in range(size)]
        # dp array to track the results
        dp = [0 for i in range(n)]
        # first ugly number is 1
        dp[0] = 1 

        for i in xrange(1,n):
            min_val = float("INF")
            for j in xrange(0, size):
                min_val = min(min_val, dp[index[j]]*primes[j])

            dp[i] = min_val

            for j in xrange(0, size):
                if min_val%primes[j]==0:
                    index[j] += 1

        return dp[n-1]

# sol = Solution()
# n = 12
# primes = [2, 7, 13, 19]
# print sol.nthSuperUglyNumber(n, primes)