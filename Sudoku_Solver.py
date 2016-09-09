class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        self.dfs(board, 0, 0)
   
    def dfs(self, board, x, y):
        if x == 9:
            return self.dfs(board, 0, y + 1)
        
        if y == 9:
            return True
        
        if board[y][x] != ".":
            return self.dfs(board, x + 1, y)
            
        else:
            for num in xrange(1, 10):
                if self.is_valid(board, x, y, str(num)):
                    board[y][x] = str(num)
                    if self.dfs(board, x + 1, y):
                        return True
                    board[y][x] = "."
        
        return False
        
    def is_valid(self, board, x, y, num):
        # check the row
        for nx in xrange(9):
            if nx != x and board[y][nx] == num:
                return False
                
        # check the column
        for ny in xrange(9):
            if ny != y and board[ny][x] == num:
                return False
        
        # check the rectangle
        nx = int(x/3) * 3
        ny = int(y/3) * 3
        
        for j in xrange(ny, ny + 3):
            for i in xrange(nx, nx + 3):
                if i == x and j == y:
                    continue
                
                if board[j][i] == num:
                    return False
        
        return True

    
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
sol = Solution()
for j in xrange(len(board)):
    row = list(board[j])
    board[j] = row

sol.solveSudoku(board)

