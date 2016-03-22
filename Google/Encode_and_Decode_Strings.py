class Codec:

    def encode(self, strs):
		"""Encodes a list of strings to a single string.

		:type strs: List[str]
		:rtype: str
		"""
		size = len(strs)
		if size == 0:
			return ""

		res = ""

		for s in strs:
			res += "%d#%s"%(len(s), s)

		return res
		
    def decode(self, s):
		"""Decodes a single string to a list of strings.

		:type s: str
		:rtype: List[str]
		"""
		size = len(s)
		if size == 0:
			return []
		
		res = []
		start, i = 0, 1
		while i<=size:
			pos = s.find('#', start)
			if pos<0:
				break
			print s[start : pos]
			length = int(s[start : pos])
			string = s[pos+1 : pos+length+1]
			res.append(string)
			start = start+length+2
			i += 1
			
		return res

# Your Codec object will be instantiated and called as such:
codec = Codec()
# strs = ["123", "abc", "789", "five guys", "#5#3###"]
strs = ["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
coded = codec.encode(strs)
print coded
print ""
print codec.decode(coded)