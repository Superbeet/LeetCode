class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        # Statement: dp[i][j] => sum by far
        # Function: dp[i][j] 
        #    = max(dp[i-1][j], dp[i][j-1]) + mtx[i][j] if mtx[i][j] < 1
        #    = 0 if mtx[i][j] == 1
        # Initial: dp[i][0] = mtx[i][0], dp[0][j] = mtx[0][j]
        
        grid = obstacleGrid
        if not grid:
            return 0
        
        height = len(grid)
        width = len(grid[0])
        dp = [[0 for j in range(width)] for i in range(height)]
        
        for j in xrange(0, width):
            if grid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
            
        for i in xrange(0, height):
            if grid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
            
        for i in xrange(1, height):
            for j in xrange(1, width):
                if grid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[height-1][width-1]
            

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