		
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		
		start_index = 0
		length = 0
		
		if s is None or s is "":
			return ""
		
		if len(s)<=1:
			return s
		
		for i in range(0, len(s)-1):
			if s[i] == s[i+1]:
				start = i
				end = i + 1
				
				temp_start_index, temp_length = self.search(s, start, end)
				
				if temp_length>length:
					length = temp_length
					start_index = temp_start_index	

			start = i
			end = i
			temp_start_index, temp_length = self.search(s, start, end)
			
			if temp_length>length:
				length = temp_length
				start_index = temp_start_index
		
		return s[start_index: start_index+length]
		
	def search(self, s, start, end):
		dist = 1
		while start-dist >= 0 and end+dist < len(s):
			if s[start-dist] is not s[end+dist]:
				break
			dist += 1
		width = end - start + 2*dist - 1
		start_index = start - dist + 1
		return [start_index, width]

			
if __name__ == '__main__':
	solution = Solution()
	
	test_list = ["abcbalmln", "", "a"]
	
	for i in test_list:
	
		result = solution.longestPalindrome(i)
		
		print "input->%s, output->%s" %(i, result)
		
		
        