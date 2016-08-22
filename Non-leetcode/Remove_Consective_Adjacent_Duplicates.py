"""
Recursively remove all adjacent duplicates

Input:  azxxzy
Output: ay
First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, 
so it is further reduced to "ay".

Input: geeksforgeeg
Output: gksfor
First "geeksforgeeg" is reduced to "gksforgg". The string "gksforgg" contains 
duplicates, so it is further reduced to "gksfor".

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac

http://blog.csdn.net/cshaxu/article/details/12835925
"""

"""
Time - O(n^2)

T(n)=T(n-2)+O(n);
T(n)=a*T(n-b)+F(n)
by Master theorem it is O(n^k+1)
which is O(n^2);

"""
def remove_duplicates(string):
	if not string:
		return ""

	new_str = ""
	i = 1
	while i < len(string):
		if string[i-1] != string[i]:
			new_str += string[i-1]
		else:
			while i < len(string) and string[i-1] == string[i]:
				i += 1
		i += 1
	# if while loop was not end because of skipping duplicated chars
	if i == len(string):
		new_str += string[i-1]

	if len(new_str) != len(string):
		return remove_duplicates(new_str)
	else:
		return new_str

# assert remove_duplicates('geeksforgeeg') == "gksfor"
# assert remove_duplicates('azxxzy') == "ay"
# assert remove_duplicates('caaabbbaacdddd') == ""
# assert remove_duplicates('acaaabbbacdddd') == "acac"
# assert remove_duplicates('aa') == "" 

"""
Time - O(n)
"""

def remove_duplicates_iter(string):
	j = -1
	i = 0
	s = list(string)
	size = len(string)
	while i < size:
		# print "i-%s j-%s => %s" %(i, j, "".join(s))
		if j == -1 or s[j] != s[i]:
			j += 1
			s[j] = s[i]
			i += 1
		else:
			while i < size and s[j] == s[i]:
				i += 1
			j -= 1
	
	return "".join(s[:j+1])

def remove_duplicates_iter(string):
	if not string:
		return ""
	print "".join(string)
	s = list(string)
	size = len(s)
	i, j = 0, -1
	for i in xrange(0, size):
		if i < size -1 and s[i] == s[i+1]:
			continue

		if i >= 1 and s[i] == s[i-1]:
			continue
		# Why?
		if j >= 0 and s[i] == s[j]:
			j -= 1
			continue

		j += 1
		s[j] = s[i]
		print "".join(s)
	
	return "".join(s[:j+1])

assert remove_duplicates_iter('geeksforgeeg') == "gksfor"
assert remove_duplicates_iter('azxxzy') == "ay"
assert remove_duplicates_iter('caaabbbaacdddd') == ""
assert remove_duplicates_iter('acaaabbbacdddd') == "acac"
assert remove_duplicates_iter('aa') == "" 