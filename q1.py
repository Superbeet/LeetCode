# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class HashTable(object):
	def __init__(self):
		self.hash_table = {}
		
	def put(self, key, value):
	
		self.hash_table.update({key:value})
		
	def get(self, key):
		
		return self.hash_table[key]
		
	def containKey(self, key):
		
		if key in self.hash_table.keys():
			
			return True
		
		else:
			
			return False

class Solution(object):
	def twoSum_brute(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		
		for n in nums:
			nums
		
		for index1 in range(0, len(nums)):
		
			for index2 in range(index1+1, len(nums)):
					
				if target  == (nums[index1] + nums[index2]):
				
					return [index1+1, index2+1]

		return None

	def twoSum(self, nums, target):

		result = []

		hash_table = HashTable()

		for index1 in range(0, len(nums)):
			
			if hash_table.containKey(nums[index1]):
				
				index2 = hash_table.get(nums[index1])
				
				if index1 < index2:
					return [index1+1, index2+1]
				else:
					return [index2+1, index1+1]
					
			else:
				
				hash_table.put(target - nums[index1], index1)

		return None
	
if __name__ == '__main__':
	solution = Solution()
	result = solution.twoSum([-1,-2,-3,-4,-5], -8)
	if result:
		index1, index2 = result
		print "index1=%d, index2=%d" %(index1, index2)
	else:
		print "No found"