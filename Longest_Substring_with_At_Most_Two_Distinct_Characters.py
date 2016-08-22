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
		
		hashmap = {}
		for j in xrange(len(s)):
			if s[j] not in hashmap:
				hashmap[s[j]] = 1
				count += 1
		
		if count<k:
			print "No enough distinct characters"
			return 0
				
		for i in xrange(len(s)):
			c = s[i]
			if c in hashmap:
				hashmap[c] += 1
			else:
				hashmap[c] = 1
				while len(hashmap)>k:
					start_char = s[start]
					if hashmap[start_char]>1:
						hashmap[start_char] -= 1
					else:
						del hashmap[start_char]
					start += 1
					
			max_len = max(max_len, i-start+1)

		return max_len

# At Most two distinct characters
# If string is very long and full of duplication letters and k is very small
# Or if we only have iterative which allows us to fetch one letter at a time
class Solution(object):
	def lengthOfLongestSubstringTwoDistinct(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		start = 0
		max_len = 0
		size = len(s)
		hashmap = {}

		for i in xrange(size):
			c = s[i]
			hashmap[c] = i
			min_last_pos = size-1
			if len(hashmap)>2:
				for char, last_pos in hashmap.iteritems():
					if last_pos < min_last_pos:
						min_last_pos = last_pos
						last_pos_char = char
				del hashmap[last_pos_char]
				start = min_last_pos+1

			# hashmap[c] = i
			max_len = max(max_len, i-start+1)

		return max_len
		
sol = Solution()
print sol.lengthOfLongestSubstringTwoDistinct("aaaa")
print sol.lengthOfLongestSubstringTwoDistinct("abcd")
print sol.lengthOfLongestSubstringTwoDistinct("aabc")


