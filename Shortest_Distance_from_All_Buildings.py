"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
"""
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
           return -1
        n = len(grid[0])
        building_num = 0

        for j in xrange(0, m):
            for i in xrange(0, n):
                if grid[j][i]==1:
                    building_num += 1

        def doBFS(grid, m, n, j, i, dist, nums):
            queue = []
            queue.append((j, i))
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            visited = {}
            level = 0
            count = 0
            while len(queue):
                level += 1
                size = len(queue)
                for i in xrange(0, size):
                    y,x = queue.pop(0)
                    for dy,dx in dirs:
                        ny = y + dy
                        nx = x + dx
                        if 0<=ny<m and 0<=nx<n and ((ny,nx) not in visited):
                            visited[(ny,nx)] = True
                            if grid[ny][nx]==0:
                                queue.append((ny, nx))
                                dist[ny][nx] += level
                                nums[ny][nx] += 1
                            elif grid[ny][nx]==1:
                                count+=1
            return count == building_num

        # Distance amount to all buildings from a node
        dist = [[0 for i in range(n)] for j in range(m)]
        # Amount of building can be reached starting from a node
        nums = [[0 for i in range(n)] for j in range(m)]

        for j in xrange(0, m):
            for i in xrange(0, n):
                if grid[j][i]==1:
                    if not doBFS(grid, m, n, j, i, dist, nums):
                        return -1

        import sys
        min_val = sys.maxint

        for j in xrange(0, m):
            for i in xrange(0, n):
                if grid[j][i]==0 and dist[j][i]!=0 and nums[j][i]==building_num:
                    min_val = min(min_val, dist[j][i])

        if min_val<sys.maxint:
           return min_val

        return -1

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
sol = Solution()
print sol.shortestDistance(grid)