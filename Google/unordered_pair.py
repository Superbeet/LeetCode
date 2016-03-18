# -*- coding: utf-8 -*-  
"""
求array 里unordered pair的数量(前一个数比后一个数大)比如{1, 3, 2}里面有一个(3, 2), {1, 2, 
3}里面没有, {3, 2, 1}里面有三个(3, 2) (3, 1) (2, 1)
{3,2,1,4} - 3,2|2,1|3,1

1. brutforce O(n*n)
2. 
"""

import copy
def merge_sort(my_array):
	if len(my_array)<=1:
		return 0

	mid = len(my_array)/2
	left_count = merge_sort(my_array[0:mid])
	right_count = merge_sort(my_array[mid:])
	count_merge = merge(my_array, my_array[0:mid], my_array[mid:])
	total = left_count + right_count + count_merge

	return total

def merge(my_array, left, right):
	# print left, right
	count = 0
	temp = -1000000 # negetive min int
	merge_array = []
	while left and right:
		# print "left -> %s, right -> %s" %(left[0], right[0])
		if left[0]<=right[0]:
			merge_array.append(left.pop(0))
		else:
			count += len(left)	#tricky point
			temp = right.pop(0)
			merge_array.append(temp)
	merge_array.extend(right if right else left)
	my_array = copy.deepcopy(merge_array)
	return count

print merge_sort([6, 1, 2, 3, 4 ,5])
print merge_sort([4, 3, 2, 1, 5])
print merge_sort([3, 2, 1, 4])


# def merge_sort(my_array):
# 	if len(my_array)<=1:
# 		return 0, my_array

# 	mid = len(my_array)/2
# 	left_count, left_array = merge_sort(my_array[0:mid])
# 	right_count, right_array = merge_sort(my_array[mid:])
# 	count_merge, merge_array = merge(left_array, right_array)
# 	total = left_count + right_count + count_merge

# 	return total, merge_array

# def merge(left, right):
# 	print left, right
# 	merge_array = []
# 	count = 0
# 	temp = -100
# 	while left and right:
# 		# print "left -> %s, right -> %s" %(left[0], right[0])
# 		if left[0]<=right[0]:
# 			merge_array.append(left.pop(0))
# 		else:
# 			count += len(left)	#tricky point
# 			temp = right.pop(0)
# 			merge_array.append(temp)
# 	merge_array.extend(right if right else left)
# 	return count, merge_array
