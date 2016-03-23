# -*- coding: utf-8 -*-
"""
给定一个车牌号包括字母和数字，然后给定一个dictionary，找出至少包含所有车牌里字母的最短单词。
讨论了很久算法，一直没提示，后来就说干脆你就写暴力算法吧，用hashtable做的，感觉效率很差不过是可以work的
"""
import copy

class Solution():
	def find_shortest_word(self, word ,dictionary):
		size = len(word)
		hashmap = {}
		for letter in word:
			if letter not in hashmap:
				hashmap[letter] = 1
			else:
				hashmap[letter] += 1
		
		# No need to start from first entry, start from the same length group
		for word in dictionary:
			localhashmap = copy.deepcopy(hashmap)
			for letter in word:
				if letter in localhashmap:
					# print "in->", letter, localhashmap[letter]
					if localhashmap[letter]>1:
						localhashmap[letter] -= 1
					elif localhashmap[letter]==1:
						del localhashmap[letter]
				
			if len(localhashmap)==0:
				return word
		
		return False

"""
Improved Solution

1 - Preprocessing
a - Sort words into alphabetic char arrays. Retain mapping from sorted to original word
b - Split dictionary by word length
c - Sort entries in each word length group alphabetically

2 - Function call
a - Sort the char array from word alphabetically
b - Start with group of the same length 
c - Loop through entries testing for characters until first letter of entry lexicographically greater than the first in your char array, then break. If match, then
return the original word
"""
		
dictionary = [
	"defgh",
	"defaaa",
	"defbbb",
	"defccc",
	"defcbb",
	"defcab",
]

word = "abcd"
sol = Solution()
print sol.find_shortest_word(word, dictionary)