class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        
        hashtable = {}
        
        for index, num in enumerate(nums):
            if num in hashtable:
                if index - hashtable[num] <= k:
                    return True
            hashtable[num] = index
        
        return False


from sortedcontainers import SortedSet

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t<0 or nums == None or len(nums) < 2:
            return False

        treeset = SortedSet()

        for i in xrange(len(nums)):
            # Solution 1
            subset = [x for x in treeset.irange(nums[i]-t, nums[i]+t)]
            if len(subset) > 0:
                return True
            treeset.add(nums[i])

            if i >= k:
                treeset.discard(nums[i - k])

        return False

sol = Solution()
assert sol.containsNearbyAlmostDuplicate([1,2,3,4,5,6,7,8], 2, 2) == True
assert sol.containsNearbyAlmostDuplicate([1,3,2,4], 1, 1) == True
assert sol.containsNearbyAlmostDuplicate([1,3,5,7], 1, 1) == False


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False