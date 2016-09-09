class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.right_count = 0

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        
        node = self.root
        count = 0
        while node:
            if val < node.val:
                count += node.right_count + node.count
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left

            elif val > node.val:
                node.right_count += 1
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right

            else:
                count += node.right_count
                node.count += 1
                break

        return count

class Solution(object):
    def countLarger(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        bst = BinarySearchTree()
        size = len(nums)
        result = [0 for i in xrange(size)]
        for i in xrange(size - 1, -1, -1):
            result[i] = bst.add(nums[i])
        
        return result

sol = Solution()
print sol.countLarger([5,2,6,1])
print sol.countLarger([5,4,3,2,1])
