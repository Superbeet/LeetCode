"""
"3+2*2" = 7
"""
import re

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {
                '+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.floordiv
            }
        
        expression = s.split()
        total = 0
        d = 0			# current sub equation's result
        index = 0
        opt = op['+']	# last add and sub operator

        while index<len(expression):

            elem = expression[index]

            if elem in '+-':
                total = opt(total, d)
                opt = op[elem]

            elif elem in '*/':
                index += 1
                d = op[elem](d, int(expression[index]))

            else:
                d = int(elem)

            index += 1

        return opt(total, d)