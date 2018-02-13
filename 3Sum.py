class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        nums = sorted(nums)
        
        if size<3:
            return []
        
        res = []
        for i in xrange(size-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.two_sum(nums, 0-nums[i], i+1, size-1, res)
        return res
        
    def two_sum(self, nums, target, start, end, res):
        left = start
        right = end
        
        while left<right:
            sum_val = nums[left] + nums[right]
            
            if sum_val == target:
                res.append((nums[start-1], nums[left], nums[right]))
                left += 1
                right -= 1
                
                while left<len(nums) and nums[left]==nums[left-1]:
                    left += 1
                
                while right>0 and nums[right]==nums[right+1]:
                    right -= 1
                
            elif sum_val<target:
                left += 1
            
            else:
                right -= 1

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        
        if len(numbers) < 3:
            return []
        
        nums = sorted(numbers)
        size = len(numbers)

        result = []
        
        for i in xrange(0, size - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left, right = i + 1, size - 1
            
            while left < right:
                
                cur_sum = nums[left] + nums[right]
                
                if cur_sum > target:
                    right -= 1
                
                elif cur_sum < target:
                    left += 1
                
                else:
                    result.append([nums[i], nums[left], nums[right]])        
                    left += 1
                    right -= 1
                    
                    while left > 0 and left < size and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right >= 0 and right < size and nums[right] == nums[right+1]:
                        right -= 1
                                            
        return result

sol = Solution()
# print sol.threeSum([0,0,0])                
print sol.threeSum([0,1,1])                
            