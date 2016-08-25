# Find pivot number
import sys

def find_pivot_number(nums):
	if not nums:
		return None

	size = len(nums)
	left_max = [None for i in xrange(size)]
	max_num = -sys.maxint
	for i in xrange(0, size):
		left_max[i] = max_num
		max_num = max(max_num, nums[i])

	right_min = [None for j in xrange(size)]
	min_num = sys.maxint
	for j in xrange(size-1, -1, -1):
		right_min[j] = min_num
		min_num = min(min_num, nums[j])

	result = []
	for m in xrange(size):
		if nums[m] > left_max[m] and nums[m] < right_min[m]:
			result.append(nums[m])

	return result

nums = [1,3,2,5,7,6,8]
print find_pivot_number(nums)