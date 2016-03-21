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

# 然后这题可以用四边不等式来优化，通过记录s[i][j]的最优分割点为k来将n^3优化成n^2。
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
			print (i, j)
			for k in xrange(p[i][j-1], p[i+1][j]+1):
				print "k->%s" %(k)
				if dp[i][k] + dp[k+1][j] + sums[j] - (sums[i-1] if i>0 else 0) < tmp:
					tmp = dp[i][k] + dp[k+1][j] + sums[j] - (sums[i-1] if i>0 else 0)
					min_k = k

			dp[i][j] = tmp
			p[i][j] = min_k
			
	return dp[0][size-1]

# Circular Stone Game
"""
有N堆石子，现要将石子有序的形成环形，规定如下：每次只能移动相邻的2堆石子合并，
合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

Solution:
环的长度是N，所以题目相当于有一排石子1....N+1....N，然后就可以用线性的石子合并问题的方法做了。 
有个要注意的地方，f(i, j) 总是与 f(N +ｉ, N +j) 相等的，所以可以减少一些不必要的计算。 
此题的关键在于化环为线性结构，与N个数围成一圈，连续多少个数的最大和，异曲同工。
将N结构的线性表，转换为双倍长度的2N结构的线性表，然后在2N长度的表中，截取我们需要的长度为N的部分
"""
def get_min_val_circular(stones):
	size = len(stones)
	if size == 0:
		return 0

	dp = [[None for i in range(2*size)] for j in range(2*size)]
	sums = []
	sum_val = 0

	double_stones = stones*2

	for amount in double_stones:
		sum_val += amount
		sums.append(sum_val)

	for i in xrange(2*size):
		dp[i][i] = 0

	for v in xrange(1, size):
		for i in xrange(0, 2*size-v):
			j = i+v
			dp[i][j] = float("INF")
			tmp = sums[j] - (sums[i-1] if i>0 else 0)

			for k in xrange(i, j):
				dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j] + tmp)

	# print_matrix(dp)
	min_sum = float("INF")
	for i in xrange(0, size):
		min_sum = min(min_sum, dp[i][i+size-1])

	return min_sum

"""
Tools
"""
def print_matrix(mtx):
	# print "---------Start----------"
	for row in mtx:
		line = ""
		for item in row:
			line += " %5s" %(item)
		print line
	print ""

# Optimization
# print get_min_val([1,2,3,4])
# print get_min_val([0])
print get_min_val_circular([1,2,3,4])