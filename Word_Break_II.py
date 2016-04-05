"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
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

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
sol = Solution()
print sol.wordBreak(s, d)