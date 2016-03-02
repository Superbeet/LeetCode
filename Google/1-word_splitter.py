def word_splitter(string):
	string = string.strip()
	size = len(string)
	if size == 0:
		return []
	
	quote = False
	start = 0
	end = 0
	res = []
	for end in xrange(0, size):
		# print string[end]
		if string[end]=='"':
			quote = not quote
		
		if string[end]==' ' or end==size-1:
			if not quote:
				dialog = string[start:end+1]
				res.append(dialog.strip('"'))
				start = end+1
		
	if quote:
		raise Exception("Invalid string")
		
	return res

print word_splitter('dog cat cat dog "dog cat cat dog" dog cat cat dog ')
print word_splitter('I have a "faux coat"')
print word_splitter('"faux coat" I have a')