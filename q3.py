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

			
class Solution(object):
    def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if s is None:
			return 0

		start = 0
		ans = 0
		i = 0
		
		hashmap = HashTable()

		for i in range(0, len(s)):
			
			if hashmap.containKey(s[i]):
				
				if ans < i - start:
					
					ans = i - start
				
				for j in range(start, hashmap.get(s[i])):
					
					hashmap.remove(j)
				
				if hashmap.get(s[i]) + 1 > start:
					
					start = hashmap.get(s[i]) + 1
				
			hashmap.put(s[i], i)
			
		if ans < i - start:
			
			ans = i - start

		return ans
		
if __name__ == '__main__':
	solution = Solution()
	result = solution.lengthOfLongestSubstring("c")
	print result