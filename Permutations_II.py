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

S = Solution()
print S.permuteUnique([1,1,2])