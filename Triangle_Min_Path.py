class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
                
        depth = len(triangle)
        prev = triangle[0]
        
        for i in xrange(1, depth):
            dp = [0 for i in range(i+1)]
            
            for j in xrange(i+1):
                if j == 0:
                    dp[j] = prev[j] + triangle[i][j]
                elif j == i:
                    dp[j] = prev[j-1] + triangle[i][j]
                else:
                    dp[j] = min(prev[j-1], prev[j]) + triangle[i][j]
            
            prev = dp
        
        return min(prev)
            
        
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
                
        depth = len(triangle)
        prev = triangle[0]
        
        dp = [None for i in range(depth)]
        dp[0] = triangle[0][0]
        
        for i in xrange(1, depth):
            for j in xrange(i, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            
        return min(dp)
            
        
        