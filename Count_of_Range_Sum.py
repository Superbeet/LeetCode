class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left_size = 0
        self.right_size = 0
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    elif val < root.val:
        root.left_size += 1
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right_size += 1
        root.right = insert(root.right, val)
    else:
        root.count += 1
    return root
    
def count_smaller(root, val):
    if root is None:
        return 0
    elif val < root.val:
        return count_smaller(root.left, val)
    elif val > root.val:
        return root.left_size + root.count + count_smaller(root.right, val)
    else:
        return root.left_size
        
def count_larger(root, val):
    if root is None:
        return 0
    elif val < root.val:
        return root.right_size + root.count + count_larger(root.left, val)
    elif val > root.val:
        return count_larger(root.right, val)
    else:
        return root.right_size
    
def range_size(root, low, high):
    total = root.count + root.left_size + root.right_size
    smaller = count_smaller(root, low)
    larger = count_larger(root, high)
    return total - smaller - larger
        
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        
        if lower > upper:
            return 0
        
        size = len(nums)
        sums = [0 for i in range(size + 1)]
        
        # cur_sum = 0
        for i in xrange(size):
            sums[i + 1] = sums[i] + nums[i]
            
        root = TreeNode(sums[0])
        count = 0
        results = []
        for i in xrange(1, size+1):
            result = range_size(root, sums[i]-upper, sums[i]-lower)
            count += result
            results.append(result)
            insert(root, sums[i])
        
        return count

'''
FenwickTree
'''
class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0]*(n+1)
        self.n = n
    
    def lowbit(self, x):
        return x & -x
    
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
    
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
    
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0
        
        sum_array = [upper, lower - 1]
        total = 0
        
        for num in nums:
            total += num
            sum_array += [total, total + lower - 1, total + upper]
        
        index = {}
        for i, x in enumerate(sorted(set(sum_array))):
            index[x] = i + 1
        
        tree = FenwickTree(len(index))
        ans = 0
        for i in xrange(len(nums)-1, -1, -1):
            tree.add(index[total], 1)
            total -= nums[i]
            ans += tree.sum(index[upper+total]) - tree.sum(index[lower+total-1])
        return ans
