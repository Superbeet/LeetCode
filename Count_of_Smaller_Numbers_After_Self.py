"""
We traverse the array from right to left and insert all elements one by one 
in an AVL tree. While inserting a new key in an AVL tree, we first compare 
the key with root. If key is greater than root, then it is greater than all 
the nodes in left subtree of root. So we add the size of left subtree to the 
count of res element for the key being inserted. We recursively follow the 
same approach for all nodes down the root.
"""
class Solution(object):
    def countres(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [0 for i in range(size)]
        bst = BinarySearchTree()
        for i in xrange(size-1, -1, -1):
            res[i] = bst.insert(nums[i])
        return res

class TreeNode(object):
    def __init__(self, val):
        self.left_cnt = 0
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0

        root = self.root    
        cnt = 0
        while root:
            if val<root.val:
                root.left_cnt += 1

                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left

            elif val>root.val:
                cnt += root.left_cnt + root.cnt

                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right

            else:
                cnt += root.left_cnt
                root.cnt += 1
                break

        return cnt

class Solution(object):
    def countSmaller(self, nums):
        
        def sort(enum):
            half = len(enum) / 2
            
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j >= n:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    elif i >= m:
                        enum[i+j] = right[j]
                        j += 1
                    elif left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1    
            return enum
            
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])  
                for i in range(len(enum))[::-1]:
                    if not left:
                        enum[i] = right.pop()
                    elif not right:
                        enum[i] = left.pop()
                    elif left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop() 
                    else:
                        enum[i] = right.pop()   
            return enum
            
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller