class Solution(object):
    def same_subset_sum(self, nums):
        if not nums:
            return 0
    
        set_sum = sum(nums)
        if set_sum%2!=0:
            return 0
            
        target = set_sum/2
        nums = sorted(nums)
        
        self.count = 0
        self.count_subset(nums, 0, 0, target)
        
        return self.count
        
    def count_subset(self, nums, index, sum_val, target):
        if index == len(nums):
            return
        
        for i in xrange(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue

            if sum_val==target:
                self.count += 1
                
            temp = sum_val
            self.count_subset(nums, i+1, sum_val+nums[i], target)
            sum_val = temp


class Solution(object):
    def same_subset_sum(self, nums):
        if not nums:
            return 0
    
        set_sum = sum(nums)
        if set_sum%2!=0:
            return 0
            
        target = set_sum/2
        nums = sorted(nums)
        print "nums->", nums
        
        self.count = 0
        self.count_subset(nums, 0, 0, target, "")
        
        return self.count
        
    def count_subset(self, nums, index, sum_val, target, express):
        if index == len(nums):
            return
        
        for i in xrange(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue

            if sum_val==target:
                print express[:-1]
                self.count += 1
                
            temp = sum_val
            tmp_express = express
            self.count_subset(nums, i+1, sum_val+nums[i], target, express+"%s+"%(nums[i]))
            sum_val = temp
            express = tmp_express

sol = Solution()
print sol.same_subset_sum([1,2,3,1,2,3])