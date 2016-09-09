import os

def get_side_length(matrix, i, j):
	if matrix is None or len(matrix) == 0:
		return 0

	h = len(matrix)
	w = len(matrix[0])

	side_length = [0]
	dfs(matrix, w, h, i, j, matrix[j][i], set([]), side_length)
	return side_length[0]

def dfs(matrix, w, h, x, y, color, visited, side_length):
	# Adjust results
	if x < 0 or x >= w or y < 0 or y >= h:
		side_length[0] +=1
		return

	if matrix[y][x] != color:
		side_length[0] += 1
		return


	dirs = [(-1,0), (1,0), (0,1), (0,-1)]
	for dx, dy in dirs:
		nx = x + dx
		ny = y + dy
				
		visited.add((y,x))
		if (ny, nx) not in visited:
			dfs(matrix, w, h, nx, ny, color, visited, side_length)
		visited.remove((y,x))

mtx1 = [
	[2,2],
	[1,1],
	[2,2]
]

mtx2 = [
	[2,2,2,2],
	[2,1,1,2],
	[2,2,2,2]
]

mtx3 = [
	[2,2,2,2],
	[2,1,1,1],
	[2,2,2,1],
	[2,1,1,1],
	[2,2,2,2]
]

assert get_side_length(mtx1, 1, 1) == 6
assert get_side_length(mtx2, 1, 1) == 6
assert get_side_length(mtx3, 1, 1) == 16