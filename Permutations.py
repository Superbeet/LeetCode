import copy
import collections

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None or len(nums)==0:
            return 0
        
        self.sol = []
        results = collections.deque([])
        self.generate(nums, results)
        return self.sol
        
    def generate(self, nums, results):
        if len(nums)==0:
            self.sol.append(results)
        
        for i in xrange(0, len(nums)):
            results.append(nums[i])
            temp = nums.pop(i)
            self.generate(copy.deepcopy(nums), copy.deepcopy(results))
            nums.insert(i, temp)
            results.pop()
            
            