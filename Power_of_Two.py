"""
8     = 0X1000
7     = 0x0111
8 & 7 = 0X0000
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        else:
            return n & (n-1) == 0

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        while True:
            if n == 1:
                return True
            elif n%2 == 1:
                return False
            else:
                n /= 2