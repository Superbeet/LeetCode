import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        num = [False] + [True]*(n-1)
        res = 0
        limit = int(math.sqrt(n))+1
        
        for i in range(2, limit):
            if num[i-1]:
                for j in range(i*i, n, i):
                    num[j-1] = False
        
        for k in range(0, n-1):
            if num[k]:
                res += 1
		
        return res
        
sol = Solution()
print sol.countPrimes(100)