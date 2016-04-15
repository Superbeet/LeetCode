def is_matrix_symmetric(matrix):
	h = len(matrix)
	w = len(matrix[0])
	for j in xrange(h):
		for i in xrange(j):
			if matrix[j][i] == matrix[i][j]:
				return False
	return True