class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n == 0:
            return 1.0
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x
        
        sqrt = self.myPow(x, n/2)
        
        if n%2 == 0:
            return sqrt*sqrt
        else:
            return sqrt*sqrt*x