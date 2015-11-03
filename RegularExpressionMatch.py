import timeit

class Solution(object):
	def isMatch(self, s, p):
		if len(s) == 0 and len(p) == 0:
			return False
		
		return self.isMatchRec(s, p, 0, 0)

	def isMatchRec(self, s, p, i, j):

		# THE BASE CASE:End of the string 
		if j == len(p):
			return i == len(s)
		
		# The first Case: next node in P is *
		if j < len(p)-1 and p[j+1] == '*':
			
			# P can skip 2 node, and the S can skip 0 or more characters.

			# match 0
			if self.isMatchRec(s, p, i, j+2):
				return True
			
			# match 1 or more
			for x in xrange(i, len(s)):
				# the char is not equal
				if not self.charMatch(s[x], p[j]):
					return False
				
				if self.isMatchRec(s, p, x+1, j+2):
					return True
					
				x+=1
				
			return False
				
		# S should have at least one character left.
		if i<len(s) and self.charMatch(s[i], p[j]):
			return self.isMatchRec(s, p, i+1, j+1)
		else:
			return False

	def charMatch(self, s_element, p_element):
		
		if s_element==p_element or p_element=='.':
			return True
			
		return False
		
sol = Solution()
from time import clock
start = clock()
result = sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
# result = sol.isMatch("aaabc", "a*bc")
finish = clock()
print "%s(s)" %(finish-start)
print result


		
		



















class Solution(object):
	def isMatch(self, s, p):
	
		def checkMatch(s, p, i, j):
			if j == len(p):
				if i == len(s):
					return True
				else:
					return False
					
			if j==len(p)-1 or p[j+1]!='*':
				if i==len(s) or (p[j]!=s[i] and p[j]!='.'):
					return False
				
				return checkMatch(s, p, i+1, j+1)
			
			# if j<len(p)-1 and p[j+1]=='*'
			
			while i<len(s) and (p[j]==s[i] or p[j]=='.'):
				if checkMatch(s, p, i, j+2):
					return True
				i+=1
			
			# if '*' means 0
			return checkMatch(s, p, i, j+2)
			
		return checkMatch(s, p ,0, 0)
		
# s[i] = abc   aaaabc
# p[j] = ab*.  a*abc

# s[i] = "ab"
# p[j] = ".*c"