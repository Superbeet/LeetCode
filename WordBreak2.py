class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""
		self.res = []
		self.dfs(s, wordDict, '')
		return self.res

	def check(self, s, word_dict):
		n = len(s)
		possible = [False]*(n+1)
		possible[0] = True
		
		for i in range(0, n+1):
			if s[:i] in word_dict:
				possible[i] = True
			else:
				for j in range(0, i):
					if possible[j] and s[j:i] in word_dict:
						possible[i] = True
		
		return possible[-1]

	
	def dfs(self, s, word_dict, string):
		if self.check(s, word_dict):
			if len(s) == 0:
				self.res.append(string[:-1])
			
			for i in range(1, len(s)+1):
				print s[:i]
				if s[:i] in word_dict:
					self.dfs(s[i:], word_dict, string+s[:i]+" ")		
	
sol = Solution()
s = "leetcode"
dict = ["leet", "code"]
print sol.check(s, dict)	
print sol.wordBreak(s, dict)
		
	