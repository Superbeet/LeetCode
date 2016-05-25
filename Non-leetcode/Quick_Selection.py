# Time O(n) Space O(logn)
# Return Kth largest Value
import random
class Solution:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []

        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)

        if k <= len(nums1):
            return self.findKthLargest(nums1, k)

        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))

        return pivot

# Return K largest Values
import random
class Solution:
    def findKLargest(self, nums, k):
        if not nums:
            return []

        pivot = random.choice(nums)
        # pivot = nums[0]
        nums1, nums2 = [], []
        # partition
        for num in nums:
            if num > pivot:
                nums1.append(num)

            elif num < pivot:
                nums2.append(num)

        if k <= len(nums1):
            return self.findKLargest(nums1, k)
        
        if k > len(nums1) + 1:
            return nums1 + [pivot] + self.findKLargest(nums2, k - len(nums1) - 1)
        
        return nums1 + [pivot]

sol = Solution()
alist = [54,26,93,17,77,31,44,55,20]
print sol.findKLargest(alist, 3)

# for m in xrange(1, len(alist)+1):
#     print sol.findKthLargest(alist, m)