"""
159. Longest Substring with At Most Two Distinct Characters

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example, Given s = "eceba",
T is "ece" which its length is 3.
"""
# k unique characters in a given string
class Solution(object):
	def lengthOfLongestSubstringKDistinct(self, s, k):
		"""
		:type s: str
		:rtype: int
		"""
		start = 0
		max_len = 0
		count = 0
		
		map = {}
		for j in xrange(len(s)):
			if s[j] not in map:
				map[s[j]] = 1
				count += 1
		
		if count<k:
			print "No enough distinct characters"
			return 0
				
		for i in xrange(len(s)):
			c = s[i]
			if c in map:
				map[c] += 1
			else:
				map[c] = 1
				while len(map)>k:
					start_char = s[start]
					if map[start_char]>1:
						map[start_char] -= 1
					else:
						del map[start_char]
					start += 1
					
			max_len = max(max_len, i-start+1)

		return max_len

# At Most two distinct characters
class Solution(object):
	def lengthOfLongestSubstringTwoDistinct(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		start = 0
		max_len = 0
		map = {}

		for i in xrange(len(s)):
			c = s[i]
			if c in map:
				map[c] += 1
			else:
				map[c] = 1
				while len(map)>2:
					start_char = s[start]
					if map[start_char]>1:
						map[start_char] -= 1
					else:
						del map[start_char]
					start += 1
					
			max_len = max(max_len, i-start+1)

		return max_len
		
sol = Solution()
print sol.lengthOfLongestSubstringTwoDistinct("aaaa")


