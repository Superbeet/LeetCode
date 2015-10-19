class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        up = 0
        down = n-1
        left = 0
        right = n-1
        num = 0
        direct = 0

        while True:
        	
			if direct == 0:
				for i in range(left, right+1):
					num += 1
					matrix[up][i] = num
				up += 1

			if direct == 1:
				for i in range(up, down+1):
					num += 1
					matrix[i][right] = num
				right -= 1

			if direct == 2:
				for i in range(right, left-1, -1):
					num += 1
					matrix[down][i] = num
				down -= 1

			if direct == 3:
				for i in range(down, up-1, -1):
					num += 1
					matrix[i][left] = num
				left += 1

			if num == n*n:
				return matrix

			direct = (direct+1)%4

sol = Solution()
print sol.generateMatrix(3)

