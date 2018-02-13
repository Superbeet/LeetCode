"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
# DP + Memorization time: O(n^2*k), space: O(nk), 假设k表示平均每个长度对应解的个数
class Solution(object):
    def wordBreak(self, s, wordDict):
        size = len(s)
        hashmap = {0:[]}
        hashmap[0].append("")
        
        if not self.helper(s, wordDict):
            return []

        for i in xrange(1, len(s)+1):
            for j in xrange(0, i):
                if j in hashmap and s[j:i] in wordDict:
                    if i not in hashmap:
                        hashmap[i] = []
                    for string in hashmap[j]:
                        if string == "":
                            new_string = s[j:i]
                        else:
                            new_string = string+" "+s[j:i]
                        hashmap[i].append(new_string)
                        
        return hashmap[size]
        
    def helper(self, s, word_dict):
        size = len(s)
        dp = [False for i in range(size+1)]
        dp[0] = True

        for i in xrange(1, size+1):
            for j in xrange(0, i):
                if dp[j] and (s[j:i] in word_dict):
                    dp[i] = True
                    break

        return dp[size]

sol = Solution()
# s = "catsanddog"
# d = ["cat", "cats", "and", "sand", "dog"]
# print sol.wordBreak(s, d)
s = "a"
d = ["b"]
print sol.wordBreak(s, d)


# DFS + Pruning time: O(2^n), space: O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s)
        # memo[i] is recording,
        # whether we cut at index "i", can get one of the result.
        possible = [True for i in xrange(size+1)]
        
        res = []
        self.dfs(s, wordDict, 0, possible, "", res)
        print possible

        return res
        
    def dfs(self, s, word_dict, start, possible, cur_str, res):
        size = len(s)
        
        if start == size:
            res.append(cur_str)
            return
    
        for i in xrange(start+1, size+1):
            # print possible[i], s[start:i]
            if possible[i] and (s[start:i] in word_dict):
                prev_size = len(res)
                if len(cur_str)==0:
                    self.dfs(s, word_dict, i, possible, s[start:i], res)
                else:
                    self.dfs(s, word_dict, i, possible, cur_str+" "+s[start:i], res)

                # print prev_size, len(res)
                if len(res)==prev_size:
                    possible[i] = False

# sol = Solution1()
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# d = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
# print sol.wordBreak(s, d)                    

# s = "catsanddog"
# d = ["cat", "cats", "and", "sand", "dog"]
# print sol.wordBreak(s, d)    

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