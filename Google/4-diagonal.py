"""
[1, 2, 3
4, 5, 6
7, 8, 9] 
->
[7, 12, 15, 8, 3]
"""
def get_diagonal_sums(matrix):
	m = len(matrix)
	if m == 0:
		return 0
	n = len(matrix[0])
	res = []
	for j in xrange(m-1, -1, -1):
		res.append(diagonal_sum(matrix, m, n, j, 0))
	
	for i in xrange(1, n):	#if start form zero, a duplicate will be there
		res.append(diagonal_sum(matrix, m, n, 0, i))
	
	return res
		
def diagonal_sum(matrix, m, n, x, y):
	diag_sum = 0
	while y<m and x<n:
		diag_sum += matrix[x][y]
		x += 1
		y += 1
	return diag_sum

mtx = [ [1, 2, 3],
		[4, 5, 6],
		[7, 8, 9], ]
print get_diagonal_sums(mtx)
print get_diagonal_sums([[0]])