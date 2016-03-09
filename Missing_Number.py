# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return None

#         size = len(nums)
#         max_val = 0
#         min_val = nums[0]
#         sum_val = 0

#         for i in xrange(0, size):
#             sum_val += nums[i]
#             max_val = max(max_val, nums[i])
#             min_val = min(min_val, nums[i])

#         sum_corr = (0 + max_val)*(max_val - 0 + 1)/2

#         if sum_corr - sum_val == 0:
#             if min_val == 0:
#                 return max_val+1
#             else:
#                 return 0

#         return sum_corr - sum_val

# 时间 O(N) 空间 O(1)
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


import unittest

class TestGroup(unittest.TestCase):

    def test_init(self):
        sol = Solution()
        # sol.check_group("abc", "bcd")
        self.assertEquals(sol.missingNumber([0,1]), 2)
        # self.assertEquals(d.b, 'test')
        # self.assertTrue(sol.check_group("abc", "bcd"))
        # self.assertTrue(sol.check_group("abc", "cde"))
        # self.assertTrue(sol.check_group("cde", "abc"))
        # self.assertTrue(sol.check_group("az", "ba"))