"""
（DFS + Memorization）
"""
class Solution1(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        h = len(matrix)
        w = len(matrix[0])
        dp = [[0 for i in range(w)] for j in range(h)]
        max_len = 1
        for j in xrange(0, h):
            for i in xrange(0, w):
                dp[j][i] = self.dfs(matrix, w, h, i, j, dp)
        return max([max(row) for row in dp])
    
    def inbound(self, w, h, i, j):
        if i >= w or i < 0 or j >= h or j < 0:
            return False
        return True

    def dfs(self, matrix, w, h, x, y, dp):
        if dp[y][x] > 0:
            return dp[y][x]
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            print x, y, nx, ny
            if self.inbound(w, h, nx, ny) and matrix[y][x] < matrix[ny][nx]:
                dp[y][x] = max(dp[y][x], self.dfs(matrix, w, h, nx, ny, dp))
        
        dp[y][x] += 1
        return dp[y][x]
        

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        height = len(matrix)

        if height == 0:
            return 0

        width = len(matrix[0])

        dp = [[0 for w in range(width)] for h in range(height)]
        
        for j in xrange(0, height):
            for i in xrange(0, width):
                if dp[j][i]==0:
                    dp[j][i] = self.doDFS(matrix, dp, height, width, j, i)

        return max([max(row) for row in dp])

    def doDFS(self, matrix, dp, h, w, y, x):
        if dp[y][x]:
            return dp[y][x]

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<w and 0<=ny<h and matrix[y][x]<matrix[ny][nx]:
                dp[y][x] = max(dp[y][x], self.doDFS(matrix, dp, h, w, ny, nx))

        dp[y][x] += 1
        return dp[y][x]

sol = Solution1()
nums = [[1,2]]
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# nums = [[0,1,2,3,4,5,6,7,8,9],
# [19,18,17,16,15,14,13,12,11,10],
# [20,21,22,23,24,25,26,27,28,29],
# [39,38,37,36,35,34,33,32,31,30],
# [40,41,42,43,44,45,46,47,48,49],
# [59,58,57,56,55,54,53,52,51,50],
# [60,61,62,63,64,65,66,67,68,69],
# [79,78,77,76,75,74,73,72,71,70],
# [80,81,82,83,84,85,86,87,88,89],
# [99,98,97,96,95,94,93,92,91,90],
# [100,101,102,103,104,105,106,107,108,109],
# [119,118,117,116,115,114,113,112,111,110],
# [120,121,122,123,124,125,126,127,128,129],
# [139,138,137,136,135,134,133,132,131,130],
# [0,0,0,0,0,0,0,0,0,0]]

print sol.longestIncreasingPath(nums)