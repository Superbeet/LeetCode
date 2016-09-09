class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []

        size = len(nums)
        t_range = [-1, -1]
        self.search_range_helper(nums, 0, size-1, target, t_range)
        return t_range


    def search_range_helper(self, array, left, right, target, t_range):
        if left>right:
            return

        mid = (left+right)/2

        if array[mid] == target:
            if mid < t_range[0] or t_range[0] == -1:
                t_range[0] = mid
                self.search_range_helper(array, left, mid-1, target, t_range)

            if mid > t_range[1] or t_range[1] == -1:
                t_range[1] = mid
                self.search_range_helper(array, mid+1, right, target, t_range)

        elif array[mid] < target:
            return self.search_range_helper(array, mid+1, right, target, t_range)

        else:
            return self.search_range_helper(array, left, mid-1, target, t_range)
