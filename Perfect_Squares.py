# Lagrange's Four-Square Theorem
# O(n*sqrt(n))
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4==0:
            n/=4
        if n%8==7:
            return 4
        a = 0
        while a**2<=n:
            b = int(math.sqrt(n-a**2))
            if a**2 + b**2 == n:
                if (a==0 and b>0) or (a>0 and b==0):
                    return 1
                else:
                    return 2
            a += 1
        return 3

# Dynamic Programming
# Time out O(n^2)
import sys, math
max_int = sys.maxint
class Solution(object):
    def numSquares(self, n):
        dp = [max_int for i in range(n+1)]
        dp[0] = 0
        for a in xrange(0, n+1):
            for b in xrange(0, int(math.sqrt(n-a)+1)):
                dp[a+b*b] = min(dp[a]+1, dp[a+b*b])
            print dp
        return dp[n] 

# Time out O(n^2)
import math, sys
class Solution2(object):
    _dp = [0]
    def numSquares(self, n):
        # dp.append(0)
        dp = self._dp
        while len(dp)<=n:
            val = sys.maxint
            m = len(dp)
            j = 1
            while j**2<=m: 
                val = min(val, dp[m-j**2]+1)
                j+=1
            dp.append(val)
        return dp[-1]

import timeit

sol = Solution2()
print sol.numSquares(1024)
# print(timeit.timeit("sol.numSquares(5673)", setup="from __main__ import sol",number=100))

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint for i in range(n+1)]
        
        dp[0] = 0
        dp[1] = 1
        
        for x in xrange(1, int(math.sqrt(n))+1):
            dp[x**2] = 1
        
        for i in xrange(2, n+1):
            for j in xrange(1, int(math.sqrt(n))+1):
                if dp[i] == 1:
                    break
                if j**2 > i:
                    break
                dp[i] = min(dp[i], dp[i-j**2] + 1)
        
        return dp[n]
            
            
            
            
            
            
            
            