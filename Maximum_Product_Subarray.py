"""
[2,3,-2,4] -> [2,3]
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        max_pos_val_global = 0
        min_neg_val_global = 0
        max_val = 0
        min_val = 0

        for i in xrange(0, size):
            if nums[i]>0:
                max_pos_val_global = (max_pos_val_global*nums[i] if max_pos_val_global!=0 else nums[i])
                min_neg_val_global = (min_neg_val_global*nums[i] if min_neg_val_global!=0 else 0)
                # max_pos_val_global = max(max_pos_val_global*nums[i], nums[i])
                # min_neg_val_global = min(min_neg_val_global*nums[i], nums[i])

            elif nums[i]<0:
                tmp = max_pos_val_global
                max_pos_val_global = min_neg_val_global*nums[i]
                min_neg_val_global = min(tmp*nums[i], nums[i])
            else:
                max_pos_val_global = 0
                min_neg_val_global = 0

            print "max_pos_val_global->", max_pos_val_global
            print "min_neg_val_global->", min_neg_val_global

            max_val = max(max_val, max_pos_val_global)
            min_val = min(min_val, min_neg_val_global)

        return max_val

sol = Solution()
# sol.maxProduct([0,2])
# sol.maxProduct([-2,1])
# sol.maxProduct([2,1])
# sol.maxProduct([2,3])
# sol.maxProduct([2,3,4])
# sol.maxProduct([1,0,-1,2,3,-5,-2])
# sol.maxProduct([-4,-3,-2])
sol.maxProduct([3,-1,4])