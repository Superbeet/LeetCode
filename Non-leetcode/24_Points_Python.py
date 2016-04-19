class Solution():
    def check_points(self, nums, target):
        self.sol = []
        res = self.search(nums, len(nums), target)
        return self.sol

    def search(self, nums, n, target):
        if n==1:
            if nums[0] == target:
                return True
            else:
                return False

        for i in xrange(0, n):
            for j in xrange(i+1, n):
                a = nums[i]
                b = nums[j]
                nums[j] = nums[n-1]

                nums[i] = a + b
                if self.search(nums, n-1, target):
                    return True

                nums[i] = a - b
                if self.search(nums, n-1, target):
                    return True

                nums[i] = b - a
                if self.search(nums, n-1, target):
                    return True

                nums[i] = a*b
                if self.search(nums, n-1, target):
                    return True

                if b!= 0:
                    nums[i] = int(a/b)
                    if self.search(nums, n-1, target):
                        return True

                if a!= 0:
                    nums[i] = int(b/a)
                    if self.search(nums, n-1, target):
                        return True

                nums[i] = a
                nums[j] = b

        return False

# class Solution():
#     def check_24_points(self, nums, target):
#         expression = [str(n) for n in nums]
#         self.sol = []
#         res = self.search(nums, expression, len(nums), target)
#         return self.sol

#     def search(self, nums, express, n, target):
#         if n==1:
#             print "nums->", nums
#             if nums[0] == target:
#                 self.sol.append(express[0])
#                 return True
#             else:
#                 return False

#         for i in xrange(0, n):
#             for j in xrange(i+1, n):

#                 a = nums[i]
#                 b = nums[j]
#                 nums[j] = nums[n-1]

#                 expa = express[i]
#                 expb = express[j]
#                 express[j] = express[n-1]

#                 express[i] = '(' + expa + '+' + expb + ')'
#                 nums[i] = a + b
#                 if self.search(nums, express, n-1, target):
#                     return True

#                 express[i] = '(' + expa + '-' + expb + ')'
#                 nums[i] = a - b
#                 if self.search(nums, express, n-1, target):
#                     return True

#                 express[i] = '(' + expa + '*' + expb + ')'
#                 nums[i] = a*b
#                 if self.search(nums, express, n-1, target):
#                     return True

#                 if b!= 0:
#                     express[i] = '(' + expa + '/' + expb + ')'
#                     nums[i] = int(a/b)
#                     if self.search(nums, express, n-1, target):
#                         return True

#                 nums[i] = a
#                 nums[j] = b
#                 express[i] = expa
#                 express[j] = expb

#         return False

# nums = [2, 3, 6, 9]
# nums = [1, 2, 4, 4]

sol = Solution()
# print sol.check_24_points([1, 2, 4, 4], 24)
print sol.check_24_points([3, 17, 2, 11], 24)
# print sol.check_24_points([1, 1, 1, 8], 24)
# print sol.check_24_points(nums, 75)