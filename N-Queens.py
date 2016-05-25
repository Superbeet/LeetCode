"""
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
# O(N!) after prunning
import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n<0:
            return []

        res = []
        row_col = [-1 for i in range(n)]
        self.place(n, 0, row_col, res)

        return res

    def printf_sol(self, size, row_col):
        sol = []
        for queen_loc in row_col:
            row_str = "."*queen_loc + "Q" + "."*(size-1-queen_loc)
            sol.append(row_str)
        return sol      

    def check_valid(self, row, col, row_col):
        for next_row in xrange(row-1, -1, -1):
            if row_col[next_row] == col:
                return False
            if abs(row - next_row) == abs(row_col[next_row] - col):
                return False
        return True

    def place(self, size, row, row_col, res):
        if row == size:
            # res.append(copy.deepcopy(row_col))
            row_str = self.printf_sol(size, row_col)
            res.append(row_str)
            return

        for col in xrange(size):
            if self.check_valid(row, col, row_col): ## Pruning
                row_col[row] = col
                self.place(size, row+1, row_col, res)
                row_col[row] = -1

def print_chessboard(chess_array):
    for chess in chess_array:
        for row in chess:
            print row
        print ""

sol = Solution()
result = sol.solveNQueens(4)
print_chessboard(result)