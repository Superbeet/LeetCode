
  # ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  # ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		stack = []

		for token in tokens:
			if token not in ['+', '-', '*', '/']:
				stack.append(token)
			else:
				if len(stack)>=2:
					num1 = int(stack.pop())
					num2 = int(stack.pop())
				else:
					return StandardError('invalid expression')

				if token is '+':
					stack.append(num1+num2)

				if token is '-':
					stack.append(num2-num1)

				if token is '*':
					stack.append(num1*num2)

				if token is '/':

					if num2 == 0:
						return ZeroDivisionError('invalid expression')

					if num1*num2>=0:
						stack.append(num2/num1)
					else:
						stack.append(-((-num2)/num1))

		return stack[0]

sol = Solution()
print sol.evalRPN(["2", "1", "+", "3", "*"])
print sol.evalRPN(["4", "13", "5", "/", "+"])