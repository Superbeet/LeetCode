

class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		result = []
		cur_str = ''

		left_num = 0
		right_num = 0
		self.combineParenthesis(result, cur_str, n, left_num, right_num)
		return result

	def combineParenthesis(self, res, cur_str,  
								n, left_num, right_num ):

		if left_num+right_num == 2*n:
			res.append(cur_str)
			return

		if left_num<n:
			cur_str += '('
			self.combineParenthesis(res, cur_str,  n, left_num+1, right_num)
			cur_str = cur_str[:-1]

		if right_num<left_num:
			cur_str += ')'
			self.combineParenthesis(res, cur_str,  n, left_num, right_num+1)
			cur_str = cur_str[:-1]


sol = Solution()
print sol.generateParenthesis(5)

    		

