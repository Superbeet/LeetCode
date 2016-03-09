class Solution(object):
	def generatePossibleNextMoves(self, s):
	    """
	    :type s: str
	    :rtype: List[str]
	    """
    
	def generate_possible_move(self, string, hashmap):
		if string is None:
			return 

		for i in xrange(0, len(string)):
			if string[i] == "+":
				string[i] == "-"
				self.generate_possible_move(string, hashmap)



		# has_plus = False
		
		# for i in xrange(0, len(string)):
		# 	if string[i] == "+":
		# 		if has_plus == True

		# 		string[i] = "-"
		# 		has_plus = True