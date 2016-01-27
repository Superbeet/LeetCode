"""
You are given a list of word. Find if two words can be joined to-gather to form a palindrome. eg Consider a list {bat, tab, cat} Then bat and tab can be joined to gather to form a palindrome.

Expecting a O(nk) solution where n = number of works and k is length 
1. add the word to trie
2. Each time we pick a word reverse it and search it in the trie.character by character
3a. If the word match but the we still dont reach the sentinel eg. input word is "h" and we already have a "hellolle" in trie. Here we match "h" and then have "ellole" to go. In such a situation we list all the words from "e" onwards which is just "ellole" in this case and check if they are palindrome. if so we have the desired pair.
3b. If a part of input reversed word matches and we reach a sentinel in trie but there is still a suffix of input reveresed remaining e.g. "leh" is in trie and we have "hellol" as new word from the input. Then we will match "hel" from reversed "leh" but "lol" is yet remaining. Here we just check if remaining portion is palindrome. if so we have the desired pair.
"""

# Time: O(nk+n) nk->process and generate the hashtable, n->check if every word exists in hastable
class Solution(object):

	def __init__(self):
		self.hash = {}
		self.result = []

	def find_palidomes(self, strings):
		
		self.post_process(strings)

		for s in strings:

			if s[::-1] in self.hash:
				for postfix in self.hash[s[::-1]]:
					self.result.append([(s[::-1]+postfix), s])

		return self.result

	def post_process(self, strings):
		
		for s in strings:

			print self.hash

			if s not in self.hash:
				self.hash[s] = [""]

			for i in xrange(1,len(s)+1):
				if self.check_palidome(s[-i:]):
					if s[:-i] not in self.hash:
						postfix = []
						postfix.append(s[-i:])
						self.hash[s[:-i]] = postfix
					else:
						self.hash[s[:-i]].append(s[-i:])

	def check_palidome(self, s):
		if s == "":
			return True

		if s == s[::-1]:
			return True

		return False

sol = Solution()
strings = ["abc","ba","ab","a", "abb"]
print sol.find_palidomes(strings)