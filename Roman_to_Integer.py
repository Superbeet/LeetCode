"""
I: 1
V: 5
X: 10
L: 50
C: 100
D: 500
M: 1000

字母可以重复，但不超过三次，当需要超过三次时，用与下一位的组合表示：
I: 1, II: 2, III: 3, IV: 4
C: 100, CC: 200, CCC: 300, CD: 400
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
        	'I': 1,
        	'V': 5,
        	'X': 10,
        	'L': 50,
        	'C': 100,
        	'D': 500,
        	'M': 1000,
        }

        if s == "":
        	return 0

        index = len(s) - 2
        sum = ROMAN[s[-1]]

        while index >= 0:
        	if ROMAN[s[index]] < ROMAN[s[index+1]]:
        		sum -= ROMAN[s[index]]
        	else:
        		sum += ROMAN[s[index]]

        	index -= 1

        return sum