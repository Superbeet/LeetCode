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
		# Tree pruning
		if self.check(s, word_dict):
			if len(s) == 0:
				self.res.append(string[:-1])
			
			for i in range(1, len(s)+1):
				if s[:i] in word_dict:
					self.dfs(s[i:], word_dict, string+s[:i]+" ")		

"""
这里加上一个possible数组，如同WordBreak I里面的DP数组一样，用于记录区间拆分的可能性

Possible[i] = true 意味着 [i,n]这个区间上有解
"""
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""
		size = len(s)
		self.possible = [True]*(size+1)

		res = ""
		sols = []
		self.get_all_solution(0, s, wordDict, size, res, sols)
		return sols

	def get_all_solution(self, start, string, dictionary, size, result, sols):
		if start == size:
			sols.append(result[:-1])
			return
		
		for i in xrange(start, size):
			segment = string[start:i+1]
			if (segment in dictionary) and self.possible[i+1]:
				pre_result = result
				pre_size = len(sols)
				result += segment + " "
				self.get_all_solution(i+1, string, dictionary, size, result, sols)
				if len(sols) == pre_size:
					self.possible[i+1] = False
				result = pre_result
					
sol = Solution()
s = "leetcode"
dict = ["leet", "code"]
print sol.check(s, dict)	
print sol.wordBreak(s, dict)