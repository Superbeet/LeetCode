# Split string by words

def split_by_space(string):
	if not string:
		return []

	size = len(string)
	left, right = 0, 0
	result = []
	for right in xrange(size):
		if string[right] != " ":
			continue
		
		if right > left:
			result.append(string[left: right])
			left = right + 1
		else:
			left = right + 1

	if left <= right:
		result.append(string[left:size])

	return result

assert split_by_space("") == []
assert split_by_space("hello world") == ["hello", "world"] 
assert split_by_space(" hello world ") == ["hello", "world"]
assert split_by_space("    a ") == ["a"]
assert split_by_space("a b c") == ["a", "b", "c"]

def reverse_by_space(string):
	if not string:
		return []

	size = len(string)
	left, right = 0, 0
	result = []
	for right in xrange(size):
		if string[right] != " ":
			continue
		
		if right > left:
			result.append(string[left: right][::-1])
			left = right + 1
		else:
			left = right + 1

	if left <= right:
		result.append(string[left:size][::-1])

	return result

assert reverse_by_space("  hello world   ") == ["olleh", "dlrow"] 