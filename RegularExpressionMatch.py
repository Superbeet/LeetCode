import timeit

class Solution(object):
	def isMatch(self, s, p):
		if len(s) == 0 and len(p) == 0:
			return False
		
		return self.isMatchRec(s, p, 0, 0)

	def isMatchRec(self, s, p, i, j):

		# End of the string 
		if j == len(p):
			return i == len(s)
		
		# At least two character left in pattern
		if j < len(p)-1 and p[j+1] == '*':
			
			# match 0
			if self.isMatchRec(s, p, i, j+2):
				return True
			
			# match 0 or more
			for x in xrange(i, len(s)):
				# match 1 0r more
				if not self.charMatch(s[x], p[j]):
					return False
				
				if self.isMatchRec(s, p, x+1, j+2):
					return True
					
				x+=1
				
			return False
					
		return i<len(s) and self.charMatch(s[i], p[j]) and self.isMatchRec(s, p, i+1, j+1)

	def charMatch(self, s_element, p_element):
		
		if s_element==p_element or p_element=='.':
			return True
			
		return False
		
sol = Solution()
from time import clock
start = clock()
# result = sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
result = sol.isMatch("aaabc", "a*bc")
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