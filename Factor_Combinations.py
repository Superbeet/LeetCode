import math
import copy

"""
The idea is to use back tracking to build the factorial combinations on the fly. Using i*i <=n will avoid expensive division operation. Also, avoid dividing the last prime number by building the final remaining n directly into the "path". Using of "start" will avoid duplications because "start" is always >= i.
"""

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        
        self.res = []
        
        self.get_all_sols(n, 2, [])
        
        return self.res
        
    def get_all_sols(self, n, start, sol):
        			
        for i in xrange(start, int(math.sqrt(n))+1):
            if n%i==0:
                sol.append(i)
                self.get_all_sols(n/i, i, copy.deepcopy(sol))
                sol.pop()
				
        if len(sol)>0:
			# building the final remaining n directly into the "path"
            sol.append(n)
            self.res.append(copy.deepcopy(sol))
            sol.pop()

sol = Solution()
print sol.getFactors(4)
print sol.getFactors(12)
print sol.getFactors(32)
print sol.getFactors(37)
print sol.getFactors(23848713)