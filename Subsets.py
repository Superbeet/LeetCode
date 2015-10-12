import copy

#Iterative
# class Solution(object):
#     def subsets(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""

# 		nums.sort()
# 		array_list = [[]]

# 		for num in nums:
			
# 			for i in range(0, len(array_list)):
				
# 				item = []
				
# 				item = copy.copy(array_list[i])
				
# 				item.append(num)
				
# 				array_list.append(item)

# 		return array_list
		

#Recursive
class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		rst = []
		now = []
		nums.sort()
		self.getSubset(nums, 0, len(nums), rst, now)
		return rst
		
	def getSubset(self, nums, index, n, rst, now):
		if index == n:
			rst.append(copy.copy(now))
			return

		# print "index->", index
		self.getSubset(nums, index+1, n ,rst, now)

		now.append(nums[index])
		self.getSubset(nums, index+1, n, rst, now)
		now.pop(-1)
		
		return
		
		
nums = [1,5,2]
sol = Solution()
print sol.subsets(nums)
			