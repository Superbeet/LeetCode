import copy
import collections

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None or len(nums)==0:
            return 0
        
        self.sol = []
        results = []
        visited = [False for i in xrange(len(nums))]
        nums = sorted(nums)
        self.generate(nums, 0, results, visited)
        return self.sol
        
    def generate(self, nums, step, results, visited):

        if step==len(nums):
            self.sol.append(results)
            return
        
        for i in xrange(0, len(nums)):
            if not visited[i]:
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                    continue
                visited[i] = True
                results.append(nums[i])
                self.generate(nums, step+1, copy.deepcopy(results), visited)
                results.pop()
                visited[i] = False

import copy

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None or len(nums)==0:
            return 0
        
        self.sol = []
        # visited = [False for i in xrange(len(nums))]
        # visited = set()
        # nums = sorted(nums)
        self.permute_helper(nums, 0)
        return self.sol
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return
    
    def permute_helper(self, nums, step):
        print step, nums
        if step==len(nums):
            self.sol.append(copy.deepcopy(nums))
            return

        used = set() #declare used set in every recursion

        for i in xrange(step, len(nums)):
            if nums[i] in used: #
                continue
        
            self.swap(nums, step, i)
            self.permute_helper(nums, step+1)
            self.swap(nums, i, step)
            used.add(nums[i])

        # print step, used, nums

S = Solution()
# print S.permuteUnique([1,1,2,3])
print S.permuteUnique([1,3,3,3])