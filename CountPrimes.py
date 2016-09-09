import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        is_prime = [True]*n
        is_prime[0] = False
        is_prime[1] = False

        res = 0
        limit = int(math.sqrt(n))+1
        
        for i in range(2, limit):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        for k in range(0, n-1):
            if is_prime[k]:
                res += 1
		
        return res
        
sol = Solution()
print sol.countPrimes(100)