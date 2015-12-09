"""
Problem 2: An sorted array n - 1 unique numbers in the range from 0 to n - 1. There is only one number in the range from 0 to n - 1 missing. Please write a function to find the missing number. 

Analysis: Of couse, we could use the solution above to solve this problem, which costs O(n) time. This solution does not utilize the properties of sorted arrays. 

Since numbers from 0 to n - 1 are sorted in an array, the first numbers should be same as their indexes. That's to say, the number 0 is located at the cell with index 0, the number 1 is located at the cell with index 1, and so on. If the missing number is denoted as m. Numbers less then m are located at cells with indexes same as values.

The number m + 1 is located at a cell with index m, The number m + 2 is located at a cell with index m + 1, and so on. We can see that, the missing number m is the first cell whose value is not identical to its value.

Therefore, it is required to search in an array to find the first cell whose value is not identical to its value. Since the array is sorted, we could find it in O(lgn) time based on the binary search algorithm as implemented below:

int getOnceNumber_sorted(int* numbers, int length)
{
    if(numbers == NULL || length <= 0)
        return -1;

    int left = 0;
    int right = length - 1;
    while(left <= right)
    {
        int middle = (right + left) >> 1;
        if(numbers[middle] != middle)
        {
            if(middle == 0 || numbers[middle - 1] == middle - 1)
                return middle;
            right = middle - 1;
        }
        else
            left = middle + 1;
    }
   
    if(left == length ) // corrected by Kyunghee Kim
        return length;

    return -1;
}

"""
class Solution(object):
    def missingNumberInSortedArray(self, nums):
        length = len(nums)
        left = 0
        right = length - 1

        if nums == None or length <= 0:
            return -1

        while left<=right:

            middle = (left + right)/2

            if nums[middle] != middle:
                if middle == 0 or nums[middle-1] == middle-1:
                    return middle

                right = middle - 1

            else:

                left = middle + 1

        if left == length:
            return length

        return -1


import unittest

class TestGroup(unittest.TestCase):

    def test_init(self):
        sol = Solution()
        # sol.check_group("abc", "bcd")
        self.assertEquals(sol.missingNumberInSortedArray([0,1,2,3,4,5,7]), 6)