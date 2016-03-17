"""
Given heights of n persons standing in a line and a list of numbers corresponding to each person (p) that gives the number of persons who are taller than p and standing in front of p. For example,
Heights: 5 3 2 6 1 4
InFronts:0 1 2 0 3 2
Means that the actual actual order is: 5 3 2 1 6 4
The question gets the two lists of Heights and InFronts, and should generate the order standing in line.
"""

def restore_the_line(person_list, height_list):
	if not person_list or not height_list or len(person_list)!=len(height_list):
		return 
	
	size = len(person_list)
	hash = {}
	
	person_list = sorted(person_list)
	result = [None for x in range(size)]
	
	for i in xrange(0, size, 1):
		for j in xrange(size-1, -1, -1):
			if height_list[j]==0 and not j in hash:
				result[j] = person_list[i]
				hash[j] = True
				break
			else:
				height_list[j] -= 1
	
	return result
	
	
A = [5, 3, 2, 6, 1, 4]
B = [0, 1, 2, 0, 3, 2]
print restore_the_line(A, B)
	
			
			
			