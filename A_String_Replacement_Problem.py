def check_match(orig, start, pattern):
	if orig is None or pattern is None:
		return False

	size = len(orig)
	length = len(pattern)
	i, j = start, 0
	while i<size and j<length:
		if orig[i] != pattern[j]:
			return False
		i += 1
		j += 1

	if j == length:
		return True
	else:
		return False

def str_replace(orig, pattern, replace):
	if orig is None or pattern is None or replace is None:
		raise Exception("")

	orig_size = len(orig)
	pattern_size = len(pattern)
	replace_size = len(replace)

	new_str = ""
	fast = 0

	while fast < orig_size:

		is_match = False

		while True:
			if not check_match(orig, fast, pattern):
				break
			is_match = True
			fast += pattern_size

		if is_match:
			new_str += replace

		if fast < orig_size:
			new_str += orig[fast]

		fast += 1

	print new_str
	return new_str

print check_match("a", 0, "a")

str_replace("a", "a", "X")
str_replace("a", "a", "XYZ")
str_replace("aa", "aaa", "X" )
str_replace("a", "a", "X" )
str_replace("abcabc", "abc", "X" )
str_replace("abcabcabc", "abc", "X" )
str_replace("abcaabcaabc", "abc", "X" )
str_replace("abcaaabcaaabca", "abc", "X" )
str_replace("abcabcabababcabc", "abc", "X" )
str_replace("abcabcabababcabcab", "abc", "X" )
str_replace("aabbaabbaaabbbaabb", "aabb", "X" )
				






