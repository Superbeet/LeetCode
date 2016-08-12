"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""
import copy
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        result = []
        candidates = sorted(candidates)
        self.build_combination(candidates, target, 0, 0, [], result)
        return result
    
    def build_combination(self, candidates, target, start, sum, ans, res):
        if sum > target:
            return
        
        if sum == target:
            res.append(copy.deepcopy(ans))
            return
        
        for i in xrange(start, len(candidates)):
            prev_sum = sum
            sum += candidates[i]
            ans.append(candidates[i])
            self.build_combination(candidates, target, i, sum, ans, res)
            sum = prev_sum
            ans.pop()

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.
"""
import copy
class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        result = []
        candidates = sorted(candidates)
        self.build_combination(candidates, target, 0, 0, [], result)
        return result
    
    def build_combination(self, candidates, target, start, sum, ans, res):
        if sum > target:
            return
        
        if sum == target:
            res.append(copy.deepcopy(ans))
            return
        
        for i in xrange(start, len(candidates)):
            if i > start and candidates[i-1] == candidates[i]:
                continue
            
            prev_sum = sum
            sum += candidates[i]
            ans.append(candidates[i])
            self.build_combination(candidates, target, i+1, sum, ans, res)
            sum = prev_sum
            ans.pop()