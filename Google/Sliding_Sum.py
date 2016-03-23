"""
Input is an array of numbers and a window size k, 
Output is the the maxmium sum of all windows - (start, end)
"""
class Solution():
	def sliding_sum(self, nums, k):
		size = len(nums)
		if k>size:
			return sum(nums)

		res = []

		sum_val = sum(nums[0:k])
		res.append(sum_val)
		
		for i in xrange(1, size-k+1):
			sum_val = sum_val-nums[i-1]+nums[i+k-1]
			res.append(sum_val)

		return res

nums = [1,2,3,4,5,6,7,8,9,10]
sol = Solution()
print sol.sliding_sum(nums, 3)
			
		