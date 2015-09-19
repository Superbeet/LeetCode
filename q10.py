# Regular Expression Matching

# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

# 思路：动态规划
# 字符串s : s1s2s3...sm 模式串p: p1p2p3...pn
# 最优子结构：如果sm与pn相同或者pn为'.'，问题归为判断字符串s1s2s3...sm-1 与p1p2p3...pn-1是否匹配子问题。如果pn为'*'，那么如果'*'表示0个之前元素，问题归为判断s1s2s3...sm与p1p2p3...pn-2是否匹配子问题。如果'*'表示1个以上的之前元素，当sm与pn-1相同或者pn-1为'.'时，问题归为判断s1s2s3...sm-1与p1p2p3...pn是否匹配子问题。
# 终结条件：当字符串s为空时，模式串为空是为真，或者模式串长度为奇数为假，否则判断偶数位是否为'*'。

class Solution(object):

	def isMatch(self, s, p):
		if len(s) == 0:
			if len(p) % 2 == 1:
				return False
				
			if len(p) == 0:
				return True
			elif p[-1] == '*':
				return self.isMatch(s, p[0:-2])
			else:
				return False
				
		elif len(p) == 0:
			return False
			
		elif s[-1] == p[-1] or p[-1] == '.':
			return self.isMatch(s[0:-1], p[0:-1])
			
		elif p[-1] == '*':
			if len(p) == 1:
				return False
			elif self.isMatch(s, p[0:-2]):
				return True
			elif s[-1] == p[-2] or p[-2] == '.':
				return self.isMatch(s[0:-1], p)
			else:
				return False
				
		else:
			return False
			
		
class Solution:
	def isMatch(self, s, p):

		if len(p)==0: 
			return len(s)==0
			
		if len(p)==1 or p[1]!='*':
		
			if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
				return False
				
			return self.isMatch(s[1:],p[1:])
			
		else:
			i=-1
			length=len(s)

			while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):

				if self.isMatch(s[i+1:],p[2:]): 
				
					return True
					
				i+=1
				
			return False