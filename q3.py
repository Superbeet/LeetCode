# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class HashTable(object):
	def __init__(self):
		self.hash_table = {}
		
	def put(self, key, value):
	
		self.hash_table.update({key:value})
		
	def get(self, key):
		
		return self.hash_table[key]
	
	def size(self):
		return len(self.hash_table)
	
	def containKey(self, key):
		
		if key in self.hash_table.keys():
			
			return True
		
		else:
			
			return False

	def clean(self):
		self.hash_table = {}
		return 1
		
	def remove(self, key):
		self.hash_table.pop(key, None)
		return 

	def __repr__(self):
		return "%s" %(self.hash_table)

	def __str__(self):
		return "%s" %(self.hash_table)
			
class Solution(object):

    def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if s is None:
			return 0

		start = 0
		length = 0

		hashmap = HashTable()

		for i in range(0, len(s)):
			
			if hashmap.containKey(s[i]):
				
				for j in range(start, hashmap.get(s[i])):
					
					hashmap.remove(s[j])
				
				start = hashmap.get(s[i]) + 1

			length = max(length, i-start+1)

			# print "start -> %s, %s -> %s, hashmap -> %s" %(start, s[i], i, hashmap)
			
			hashmap.put(s[i], i)

		return length

    def lengthOfLongestSubstring2(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if s is None:
			return 0

		start = 0
		length = 0

		hashmap = HashTable()

		for i in range(0, len(s)):
			
			if hashmap.containKey(s[i]):
				
				start = max(hashmap.get(s[i])+1, start)

			length = max(length, i-start+1)

			# print "start -> %s, %s -> %s, hashmap -> %s" %(start, s[i], i, hashmap)
			
			hashmap.put(s[i], i)

		return length

if __name__ == '__main__':
	solution = Solution()

	str_list = ["", "c", "dvdf", "aaaabbb", 
				"vqblqcb",  "wobgrovw", "abcabcaaaaaaabcde"]

	for s in str_list:
		result = solution.lengthOfLongestSubstring(s)
		print "Sol1 %s -> %d" %(s, result)
		result = solution.lengthOfLongestSubstring(s)
		print "Sol2 %s -> %d" %(s, result)