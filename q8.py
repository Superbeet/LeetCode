# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

import sys

class Solution(object):
    def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		start = 0
		num = 0
		
		if not str:
			return 0

		while str[start] == " ":
			start += 1
			
		if str[start] != "+" and str[start] != "-" and not str[start].isdigit():
			return 0

		if str[start] == "-":
			sign = -1
			start += 1
		elif str[start] == "+":
			sign = 1
			start += 1
		else:
			sign = 1

		for ch in str[start:]:
			if ch.isdigit():
				num = num*10 + int(ch)
			else:
				break
		
		if num > 2147483647 and sign == 1:
			return 2147483647

		if num > 2147483648 and sign == -1:
			return -2147483648

		if sign == 1:
			return num 
		else:
			return -num
			
		
if __name__ == '__main__':
	solution = Solution()
	
	test_list = ["abcbalmln", "123", "+1024a123", "    010"]
	
	for i in test_list:
	
		result = solution.myAtoi(i)
		
		print "input->%s, output->%s" %(i, result)
		
		
		
		
			