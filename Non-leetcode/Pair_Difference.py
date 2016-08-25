# [1,5,5,2,4,6,7] => 3

def pair_difference(nums, k):
	if not nums:
		return []

	hashtable = {}
	result = []
	for num in nums:
		if num + k in hashtable:
			result.append([num + k, num])

		if num - k in hashtable:
			result.append([num - k, num])

		if num not in hashtable:
			hashtable[num] = []

	return result


print pair_difference([1,5,5,2,2,4,6,7], 3)



