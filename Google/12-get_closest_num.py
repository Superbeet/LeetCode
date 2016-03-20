import sys

def get_closest_num(nums, key):
	start, end = 0, len(nums)
	diff, min_diff = 0, sys.maxint
	min_index = 0

	while start<=end:
		mid = (start+end)/2
		diff = abs(nums[mid]-key)
		if diff<min_diff:
			min_diff = diff
			min_index = mid 

		if nums[mid]>key:
			end = mid-1
		elif nums[mid]<key:
			start = mid+1
		else:
			break

	return min_index

print get_closest_num([1.5, 5.1, 5.5, 9, 10], 6)