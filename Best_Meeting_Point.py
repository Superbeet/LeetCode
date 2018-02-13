from collections import deque

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Do BFS from each node, use DP table to recall the sum of distances to all friends' houses
        """
        h = len(grid)
        w = len(grid[0])
        
        dp = [[0 for i in range(w)] for j in range(h)]
        
        for j in xrange(h):
            for i in xrange(w):
                if grid[j][i] == 1:
                    self.bfs(dp, w, h, i, j)
        
        min_dist = sys.maxint
        min_axis = None
        for j in xrange(h):
            for i in xrange(w):
                if dp[j][i] < min_dist:
                    min_dist = dp[j][i]
                    min_axis = (j, i)

        return min_dist
    
    def bfs(self, dp, w, h, i, j):
        queue = deque()
        queue.append((i, j))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set([])
        visited.add((i, j))
        level = -1
        while queue:
            size = len(queue)
            level += 1
            for i in xrange(size):
                x, y = queue.popleft()
                dp[y][x] += level
                # visited.add((x,y))
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < w and ny >= 0 and ny < h and ((nx,ny) not in visited):
                        queue.append((nx, ny))
                        visited.add((nx, ny))


from collections import deque

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Projection
        """
        h = len(grid)
        w = len(grid[0])
        x_axis, y_axis = [], []
        dp = [[0 for i in range(w)] for j in range(h)]
        for j in xrange(h):
            for i in xrange(w):
                if grid[j][i] == 1:
                    x_axis.append(i)
                    y_axis.append(j)
        return self.min_distance(x_axis) + self.min_distance(y_axis)
    
    def min_distance(self, axis):
        axis.sort()
        sum = 0
        mid = len(axis)/2
        for i in xrange(len(axis)):
            sum += abs(axis[i] - axis[mid])
        return sum
            