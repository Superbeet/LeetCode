def printMatrix(matrix):
    for j in xrange(0, len(matrix)):
        print matrix[j]
    print "" 

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix == []:
            return
        h = len(matrix)
        w = len(matrix[0])
        
        dp = [[0 for i in range(w)] for j in range(h)]

        for j in xrange(0, h):
            for i in xrange(0, w):
                if j == 0 and i == 0:
                    top = 0
                    left = 0
                    diag = 0

                elif j == 0:
                    top = 0
                    left = dp[j][i-1]
                    diag = 0

                elif i == 0:
                    top = dp[j-1][i]
                    left = 0
                    diag = 0
                
                else:
                    top = dp[j-1][i]
                    left = dp[j][i-1]
                    diag = dp[j-1][i-1]
                dp[j][i] = top + left - diag + matrix[j][i]

        self.dp = dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1<0 or row2<0 or col1<0 or col2<0 or col1>col2 or row1>row2:
            return

        if row1==0 and col1==0:
            top = 0
            left = 0
            diag = 0
        elif row1==0:
            top = 0
            left = self.dp[row2][col1-1]
            diag = 0
        elif col1==0:
            top = self.dp[row1-1][col2]
            left = 0
            diag = 0
        else:
            top = self.dp[row1-1][col2]
            left = self.dp[row2][col1-1]
            diag = self.dp[row1-1][col1-1]

        return self.dp[row2][col2] - (top + left - diag)

# Your NumMatrix object will be instantiated and called as such:
# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# numMatrix = NumMatrix(matrix)
# print numMatrix.sumRegion(2, 1, 4, 3)
# print numMatrix.sumRegion(1, 1, 2, 2)
# print numMatrix.sumRegion(1, 2, 2, 4)

mtx = [[-4,-5]]
numMatrix = NumMatrix(mtx)
# print numMatrix.sumRegion(0, 0, 0, 0)

# numMatrix.sumRegion(1, 2, 3, 4)