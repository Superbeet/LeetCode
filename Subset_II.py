import copy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        output = []
        
        if nums==None or len(nums)==0:
            return res
            
        res.append(output)
        nums = sorted(nums)
        
        self.generate_sub(nums, 0, res, output)
        
        return res
        
    def generate_sub(self, nums, index, result, output):
        if index == len(nums):
            return
            
        for i in xrange(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
				
            output.append(nums[i])
            result.append(copy.copy(output))
			
            self.generate_sub(nums, i+1, result, output)
            output.pop(-1)
            
sol = Solution()
print sol.subsetsWithDup([1,2,2])