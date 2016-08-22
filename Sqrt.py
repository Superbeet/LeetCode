'''
Simplified Solution
'''
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x < 0:
            return
        
        left, right = 0, x
        mid = 0
        while left + 1 < right:
            mid = (left + right)/2
            if mid*mid == x:
                right = mid
            elif mid*mid < x:
                left = mid
            else:
                right = mid
            
        if right*right <= x:
            return right
        else:
            return left
            
'''
Refined Solution
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
           
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        if x < 1:
            return self.my_sqrt_helper(x, x, 1)
        else:
            return self.my_sqrt_helper(x, 1, x)
    
    def my_sqrt_helper(self, x, low, high):
        precision = 0.00001
        mid = (low + high)/2.0
        
        if abs(mid*mid-x) < precision:
            return int(round(mid))
            
        elif mid*mid-x > 0:
            return self.my_sqrt_helper(x, low, mid)
        
        else:
            return self.my_sqrt_helper(x, mid, high)
        
sol = Solution()
print sol.mySqrt(36)