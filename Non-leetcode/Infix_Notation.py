class Solution(object):
	def infix_notation(self, notation):



	def read_num(self, ):


	def evaluate(self, s, index):
		if index == len(s):
			return 0.0

		res = 1.0

		while op=="*" or op=="/":
			num, index = self.read_num(s, index)
			
			if op=="*":
				res = res*num
			else:
				res = res/num

			op = index
			index += 1

		return res + self.evaluate(s, index-1)
		