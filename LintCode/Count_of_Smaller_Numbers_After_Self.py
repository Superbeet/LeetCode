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
			if val < root.val:
				root.left_cnt += 1
				if root.left is None:
					root.left = TreeNode(val)
					break
				root = root.left

			elif val > root.val:
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
                    if j == n or i < m and left[i][1] <= right[j][1]:
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