# -*- coding: utf-8 -*-
# Linear Stone Game 
# O(n^3)
"""
有N堆石子，现要将石子有序的合并成一堆，规定如下：每次只能移动相邻的2堆石子合并，
合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。
"""
def get_min_val(stones):
	size = len(stones)
	if size == 0:
		return 0

	dp = [[None for i in range(size)] for j in range(size)]
	sums = []
	sum_val = 0

	for amount in stones:
		sum_val += amount
		sums.append(sum_val)

	for i in xrange(size):
		dp[i][i] = 0

	for v in xrange(1, size):
		for i in xrange(0, size-v):
			j = i+v
			dp[i][j] = float("INF")
			tmp = sums[j] - (sums[i-1] if i>0 else 0)

			for k in xrange(i, j):
				dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j] + tmp)

	return dp[0][size-1]

# O(n^2)
def get_min_val_opt(stones):
	size = len(stones)
	if size == 0:
		return 0

	dp = [[float("INF") for i in range(size+1)] for j in range(size+1)]
	p = [[None for i in range(size+1)] for j in range(size+1)]
	sums = []
	sum_val = 0

	for amount in stones:
		sum_val += amount
		sums.append(sum_val)

	for i in xrange(size+1):
		dp[i][i] = 0
		p[i][i] = i

	for v in xrange(1, size):
		for i in xrange(0, size-v):
			j = i+v
			tmp = float("INF")
			k = 0
			for k in xrange(p[i][j-1], p[i+1][j]+1):
				if dp[i][k] + dp[k+1][j] + sums[j] - (sums[i-1] if i>0 else 0) < tmp:
					tmp = dp[i][k] + dp[k+1][j] + sums[j] - (sums[i-1] if i>0 else 0)
					min_k = k

			print_matrix(dp)
			dp[i][j] = tmp
			p[i][j] = min_k

	return dp[0][size-1]

def print_matrix(mtx):
	print "---------Start----------"
	for row in mtx:
		line = ""
		for item in row:
			line += " %5s" %(item)
		print line
	print ""

# Optimization
# print get_min_val([1,2,3,4])
# print get_min_val([0])

print get_min_val_opt([1,2,3,4])
# Circular Stone Game
"""
有N堆石子，现要将石子有序的形成环形，规定如下：每次只能移动相邻的2堆石子合并，
合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。
"""
