class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        if m == 0:
            return 0
            
        n = len(obstacleGrid[0])
        
        ways = [0 for i in range(n)]
        
        ways[0] = (0 if obstacleGrid[0][0]==1 else 1)
        
        for j in xrange(0, m):
            for i in xrange(0, n):
                if obstacleGrid[j][i] == 1:
                    ways[i] = 0
                elif i>0:
                    ways[i] += ways[i-1]
            
        return ways[-1]

sol = Solution()
print sol.uniquePathsWithObstacles([[0,0],[1,1]])