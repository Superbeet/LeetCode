import copy

#Iterative
class Solution1(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		nums.sort()

		array_list = [[]]

		nondup_list = []

		for num in nums:
			
			for i in range(0, len(array_list)):

				item = []
				
				item = copy.copy(array_list[i])
				
				item.append(num)
				
				array_list.append(item)

		for array in array_list:

			if array not in nondup_list:
			
				nondup_list.append(array)

		return nondup_list
		

#Recursive
class Solution2(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		rst = []
		nondup_list =[]
		now = []
		nums.sort()
		self.getSubset(nums, 0, len(nums), rst, now)

		for array in rst:
			if array not in nondup_list:
				nondup_list.append(array)

		return nondup_list
		
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

def test1():
	nums = [1,5,2,6,6,6]
	sol1 = Solution1()
	print sol1.subsetsWithDup(nums)

def test2():
	nums = [1,5,2,6,6,6]
	sol2 = Solution2()
	print sol2.subsetsWithDup(nums)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(stmt="test1()", setup="from __main__ import test1", number=10))
    print(timeit.timeit(stmt="test2()", setup="from __main__ import test2", number=10))


	# sol1 = Solution()
	# print sol1.subsetsWithDup(nums)

	# sol2 = Solution()
	# print sol2.subsetsWithDup(nums)
			