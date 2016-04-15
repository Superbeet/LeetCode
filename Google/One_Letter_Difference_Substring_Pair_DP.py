
# DP
# dp[i,j] = dp[i,j-1] && dp[i+1, j] && hash_one_letter_diff(s[i:j], s[x:y])
class Solutions(object):
	def find_substring_pairs(self, string):
		if not string:
			return 0
		
		length = len(string)
		dp = [[True for i in xrange(length+1)] for j in xrange(length+1)]
		
		total = 0
		for interval in xrange(1, length+1):
			hashmap = {}
			for start in xrange(0, length-interval+1):
				end = start + interval
				
				# Tree pruning
				if end-1>start and not dp[start:end-1] and end>start+1 and not dp[start+1:end]:
					continue
					
				count = self.count_one_letter_diff_substr(hashmap, string[start:end])
				hashmap[string[start:end]] = 1
				
				if count>0:
					dp[start][end] = True
				else: #*Unnecessary
					dp[start][end] = False
				total += count
	
		return total
		
	def count_one_letter_diff_substr(self, hashmap, substr):
		count = 0
		for i in xrange(0, len(substr)):
			for asc in xrange(97, 256):
				if chr(asc)!=substr[i]:
					temp = substr[:i] + chr(asc) + substr[i+1:]
					if temp in hashmap:
						count += 1
						print substr, "->", temp
				
		if len(substr)>1:	
			for asc in xrange(97, 256):
				temp = chr(asc) + substr[:-1]
				if temp in hashmap:
					count += 1		
					print substr, "->", temp
			
				temp = substr[1:] + chr(asc)
				if temp in hashmap:
					count += 1
					print substr, "->", temp
		
		return count

		
	# """ For reference only
	# """
	# def has_one_letter_diff(self, substr1, substr2):
		# if len(substr1)!=len(substr2):
			# raise Exception("substrs have different lengths")
		
		# diff = False
		# success = None
		# size = len(substr1)
		# i = 0
		# while i<size:
			# if substr1[i]!=substr2[i]:
				# if diff:
					# break
				# else:
					# diff = True
			# i += 1
			
		# if i == size:
			# return True
		
		# i = 1
		# while i<size:
			# if substr1[i]!=substr2[i-1]:
				# break
			# i += 1
			
		# if i == size:
			# return True
		
		# i = 1
		# while i<size:
			# if substr1[i-1]!=substr2[i]:
				# break
			# i += 1
		
		# if i == size:
			# return True
			
		# return False
		

sol = Solutions()
# print sol.has_one_letter_diff('xyabc','abcde')
# print sol.count_one_letter_diff_substr({"abcd":True, "xbcd": True, "bcde": True},'ybcd')
str = "abcabc"
print str
print sol.find_substring_pairs(str)