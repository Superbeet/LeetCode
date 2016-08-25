"""
O(n) time O(n) space
"""
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
            
        size = len(heights)
        max_height = 0
        left_max = [0 for i in range(size)]
        for i in xrange(size):
            left_max[i] = max_height
            max_height = max(max_height, heights[i])
        
        max_height = 0
        result = 0
        for j in xrange(size-1, -1, -1):
            volumn = min(left_max[j], max_height) - heights[j]
            result += volumn if volumn > 0 else 0
            max_height = max(max_height, heights[j])
            
        return result

class Solution:
    def trapRainWater(self, heights):
        if not heights:
            return 0
            
        size = len(heights)
        max_height = -sys.maxint
        left_max = [0 for i in range(size)]
        for i in xrange(size):
            left_max[i] = max_height
            max_height = max(max_height, heights[i])
        
        max_height = -sys.maxint
        right_max = [0 for j in range(size)]
        for j in xrange(size-1, -1, -1):
            right_max[j] = max_height
            max_height = max(max_height, heights[j])
        
        result = 0
        for m in xrange(size):
            volumn = min(left_max[m], right_max[m]) - heights[m]
            if volumn > 0:
                result += volumn
            
        return result

"""
O(n) time O(1) space
"""
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        if not heights:
            return 0
                  
        size = len(heights)
        result = 0        
        left, right = 0, len(heights)-1
        left_max = heights[left]
        right_max = heights[right]
        
        while left < right:
            if left_max < right_max:
                left += 1
                if heights[left] < left_max:
                    result += left_max - heights[left]
                else:
                    left_max = heights[left]
            else:
                right -= 1
                if heights[right] < right_max:
                    result += right_max - heights[right]
                else:
                    right_max = heights[right]
        
        return result