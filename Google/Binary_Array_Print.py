# -*- coding: utf-8 -*-  
"""
给string,  只包含{0,1,?}, ?可以代表0 或者1,  输出所有的组合.  
例如"10?",  输出"100", "101" 
"""

def print_binary_comb(pattern):
	size = len(pattern)
	if size == 0:
		print ""
		return
	tmp = ""
	generate_binary(pattern, tmp, size, 0)

def generate_binary(string, tmp, size, i):
	if i == size:
		print tmp
		return

	if string[i]=="?":
		generate_binary(string, tmp+"0", size, i+1)
		generate_binary(string, tmp+"1", size, i+1)
	else:
		generate_binary(string, tmp+string[i], size, i+1)

	return

print_binary_comb("???")


