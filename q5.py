

class Stack(object):
    def __init__(self, limit):
        self.queue = []
        self.limit = limit

    def push(self, item):
        if len(self.queue) is self.limit:
            return False
        else:
            self.queue.append(item)
            return True

    def pop(self):
        if len(self.queue) is 0:
            return False
        else:
            return self.queue.pop()

    def length(self):
        return len(self.queue)

    def __repr__(self):
        return "stack()"

    def __str__(self):
        return "user defined stack object %s" %(self.queue)
		
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		
		start_index = 0
		length = 0
		
		if len(s)==0:
			return ""
		
		if len(s)==1:
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
		
		print "main->", [start_index, length]
		
		return s[start_index: start_index+length]
		
	def search(self, s, start, end):
		
		dist = 1
		
		while start-dist >= 0 and end+dist < len(s):
			
			if s[start-dist] is not s[end+dist]:
				
				break
			
			dist += 1
			
		width = end - start + 2*dist - 1
		
		start_index = start - dist + 1
		
		print "search->", [start_index, width]
		
		return [start_index, width]

			
if __name__ == '__main__':
	solution = Solution()
	
	test_list = ["abcbalmln", "", "a"]
	
	for i in test_list:
	
		result = solution.longestPalindrome(i)
		
		print "input->%s, output->%s" %(i, result)
		
		
        