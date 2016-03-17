"""
{1.2, 2.5, 9.3} x = 5, return 1

Time O(log(n))
"""
import sys
import math

def find_closet_val(nums, target):
	start, end = 0, len(nums)-1
	min_diff = sys.maxint
	min_index = 0
	
	while start<=end:
		mid = (start+end)/2
		diff = abs(nums[mid]-target)
		
		if diff<min_diff:
			min_diff = diff
			min_index = mid
			
		if nums[mid]<target:
			start = mid + 1
		
		elif nums[mid]>target:
			end = mid - 1
		
		else:
			return min_index
	
	return min_index

print find_closet_val([0,0.1,0.2,0.3], 5)
print find_closet_val([1.2, 2.5, 9.3], 5)
		