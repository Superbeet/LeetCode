'''
Solution to use a list
class Solution(object):
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		
		
		self.sum_list = []

		self.getPathSum(root, 0)
		
		if sum in self.sum_list:
			return True
		
		return False
		
	def getPathSum(self, node, cur_sum):
		
		if node == None:
			return
			
		if node.left==None and node.right==None:
			self.sum_list.append(cur_sum+node.val)
		
		if node.left != None:
			self.getPathSum(node.left, cur_sum+node.val)
			
		if node.right != None:
			self.getPathSum(node.right, cur_sum+node.val)
'''

'''
Solution to directly calculate
'''
class Solution(object):
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		
		
		self.sum_list = []

		return self.getPathSum(root, 0, sum)
		
	def getPathSum(self, node, cur_sum, target_sum):
		
		if node == None:
			return False
			
		if node.left==None and node.right==None:
			return target_sum==cur_sum+node.val

		left_sum = self.getPathSum(node.left, cur_sum+node.val, target_sum)

		right_sum = self.getPathSum(node.right, cur_sum+node.val, target_sum)

		return left_sum or right_sum