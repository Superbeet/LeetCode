"""
You are given a list of word. Find if two words can be joined to-gather to form a palindrome. eg Consider a list {bat, tab, cat} Then bat and tab can be joined to gather to form a palindrome.

Expecting a O(nk) solution where n = number of works and k is length 
1. add the word to trie
2. Each time we pick a work reverse it and search it in the trie.character by character
3a. If the word match but the we still dont reach the sentinel eg. input word is "h" and we already have a "hellolle" in trie. Here we match "h" and then have "ellole" to go. In such a situation we list all the words from "e" onwards which is just "ellole" in this case and check if they are palindrome. if so we have the desired pair.
3b. If a part of input reversed word matches and we reach a sentinel in trie but there is still a suffix of input reveresed remaining e.g. "leh" is in trie and we have "hellol" as new word from the input. Then we will match "hel" from reversed "leh" but "lol" is yet remaining. Here we just check if remaining portion is palindrome. if so we have the desired pair.
"""

class Solution(object):

	def __init__(self):
		self.hash = {}

	def find_palidomes(self, strings):
		
		for s in strings:







	def check_palidome(self, s):
		if s == "":
			return True

		if s == s[::-1]:
			return True

		return False
