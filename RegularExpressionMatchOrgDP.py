class Solution():
	def isMatch(self, s, p):
		Match = [ [False for x in range(len(p)+1)] for y in range(len(s)+1) ]
		# Match[0][0] = True
		
		for i in xrange(0, len(s)+1):
			for j in xrange(0, len(p)+1):
				# 0-length P needs a 0-length S to be True 
				if j==0:
					Match[i][j] = i==0
				
				# if current char of P is *
				elif p[j-1] == '*':
					
					# there should be a char in front of *
					if j<2:
						return False
				
					for k in range(0, i+1):
						# if any consective character mismatch p[j-2], it means False
						if k!=0 and not self.is_same(s[i-k], p[j-2]):
							Match[i][j] = False
							break
						
						# if backward check the substring and get a True DP matrix element before any mismatching is found
						if Match[i-k][j-2]:
							Match[i][j] = True
							break
							
				# if current char of P is a or . (not *)
				else:
					Match[i][j] = i>=1 and Match[i-1][j-1] and self.is_same(s[i-1], p[j-1])
				
				print Match
				
		return Match[len(s)][len(p)]
		
	
	def is_same(self, s, p):
		if s==p or p == '.':
			return True
		return False
		

sol = Solution()
print sol.isMatch("aa", "a*")
# print sol.isMatch("a", "ab*a")
					
					
							
						