"""
200. Number of Islands[Medium]

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        width = len(grid[0])
        height = len(grid)
        # self.color_island(grid, width, height, 0, 0)
        count = 0
        for j in xrange(0, height):
            for i in xrange(0, width):
                if grid[j][i] == "1":
                    count += 1
                    self.color_island(grid, width, height, j, i)

        return count

    def color_island(self, grid, w, h, y, x):
        # DFS here
        if y<0 or y>=h or x<0 or x>=w:
            return

        if grid[y][x] == "2":
            return
        
        if grid[y][x] == "1":

            grid[y][x] = "2"

            for dy, dx in [(-1,0),(1,0),(0,1),(0,-1)]:
                ny = y+dy
                nx = x+dx
                self.color_island(grid, w, h, ny, nx)

        return


import unittest

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_num_of_islands(self):
        island_1 = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
        ]

        island_2 = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"],
        ]

        island_3 = [
            [u'1', u'0', u'1', u'1', u'0', u'1', u'1']
        ]

        island_4 = [
            ["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]
        ]

        island_5 = [["1","0"]]

        # self.assertEquals(self.sol.numIslands(island_1),3)
        # self.assertEquals(self.sol.numIslands(island_2),1)
        # self.assertEquals(self.sol.numIslands(island_3),3)
        self.assertEquals(self.sol.numIslands(island_4),1)
        self.assertEquals(self.sol.numIslands(island_5),1)

if __name__ == "__main__":
    unittest.main()