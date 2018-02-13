class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
            
        nums = A
        size = len(nums)
        left, right = 0, size - 1
        
        while left + 1 < right:
            mid = (left + right)/2
            
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:   # out of bound
            return right + 1
        
        # if nums[right] == target:
        #     return right
        # elif nums[left] == target:
        #     return left
        # elif target > nums[-1]:
        #     return size
        # elif target < nums[0]:
        #     return 0
        # else:
        #     return right