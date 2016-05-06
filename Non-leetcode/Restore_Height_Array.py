"""
Given heights of n persons standing in a line and a list of numbers corresponding to each person (p) that gives the number of persons who are taller than p and standing in front of p. For example,
Heights: 5 3 2 6 1 4
Ininfronts:0 1 2 0 3 2
Means that the actual actual order is: 5 3 2 1 6 4
The question gets the two lists of Heights and Ininfronts, and should generate the order standing in line.

Hint1:
Can we make the process of finding the ith empty position even more efficient ? Think binary tree / segment tree ? 
Oh, by the way, this would be a nice time to read up on Segment Trees which are incredibly useful ( http://codeforces.com/blog/entry/3327 )
What if you knew how many elements are there in first half of the array, and the second half of the array ?


Hint2:

Here, we will explore how to efficiently answer the query of finding the ith empty space.

The query can be solved using segment / interval tree.
The root contains the number of elements in [0, N].
Left node contains the number of elements in [0, N/2]
Right node contains the number of elements in [N/2 + 1, N]

Lets say we need to find the ith empty position.
We look at the number of elements X in [0, N/2].

If
    N / 2 - X >= i, the position lies in the left part of array and we move down to the left node.
    N / 2 - X < i, we now look for i - (N / 2 - X) th position in the right part of the array and move to the right node in the tree.

"""
# O(nlog(n)+n^2)=O(n^2)
def restore_the_line(heights, infronts):
    if not infronts or not heights or len(infronts)!=len(heights):
        return 
    
    size = len(infronts)
    ordered_list = sorted(zip(heights, infronts))
    heights = [x for x,y in ordered_list]
    infronts  = [y for x,y in ordered_list]

    hash = {}
    
    result = [None for x in range(size)]
    
    for i in xrange(0, size):
        for j in xrange(0, size):
            if j not in hash:
                if infronts[j]==0:
                    result[i] = heights[j]
                    hash[j] = True
                    break
                else:
                    infronts[j] -= 1
    return result

# O(n^2)
def restore_the_line_2(heights, infronts):
    if not infronts or not heights or len(infronts)!=len(heights):
        return 

    def find_empty_space(k):
        """
        Return the kth empty space
        """
        count = 0
        for j in xrange(0, size):
            if result[j]==None:
                if count==k:
                    return j
                count += 1
        return

    size = len(infronts)
    ordered_list = sorted(zip(heights, infronts))
    heights = [x for x,y in ordered_list]
    infronts  = [y for x,y in ordered_list]

    result = [None for x in range(size)]

    for i in xrange(0, size):
        pos = find_empty_space(infronts[i])
        result[pos] = heights[i]

    return result

# Time - O(n) Spcare - O(n)
def find_empty_index(k, empty_indexs):
	"""
	Return the kth empty space
	"""
	index = empty_indexs.pop(k)
	return index
		
def restore_the_line_3(heights, infronts):
	if not infronts or not heights or len(infronts)!=len(heights):
		return 
	
	size = len(heights)
	empty_index_list = range(size)

	size = len(infronts)
	ordered_list = sorted(zip(heights, infronts))
	heights = [x for x,y in ordered_list]
	infronts  = [y for x,y in ordered_list]

	result = [None for x in range(size)]

	for i in xrange(0, size):
		pos = find_empty_index(infronts[i], empty_index_list)
		result[pos] = heights[i]

	return result
    
# O(n*log(n)) n-amount of numbers log(n)-depth of tree
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.space = end - start
        self.left = None
        self.right = None

def build_tree(node):
    if node.end - node.start == 0:
        return
    mid = (node.start + node.end)/2
    node.left = Node(node.start, mid)
    node.right = Node(mid+1, node.end)
    build_tree(node.left)
    build_tree(node.right)

def find_pos(node, infront):
    node.space -= 1

    if node.left is None:
        return node.start

    if node.left.space > infront:
        return find_pos(node.left, infront)
    else:
        return find_pos(node.right, infront-node.left.space)    

def order(heights, infronts):
    if not infronts or not heights or len(infronts)!=len(heights):
        return 

    size = len(infronts)

    root = Node(0, size)
    build_tree(root)

    result = [None for x in range(size)]
    ordered_list = sorted(zip(heights, infronts))

    for (h,i) in ordered_list:
        pos = find_pos(root, i)
        result[pos] = h

    return result

# O(n) - Using an additional array to store empty space position
def find_empty_index(k, empty_index_list):
	"""
	Return the kth empty space
	"""
	index = empty_index_list.pop(k)
	return index
		
def restore_the_line_3(heights, infronts):
    if not infronts or not heights or len(infronts)!=len(heights):
        return 
	
	empty_index_list = range(size)
	print empty_index_list
	
    size = len(infronts)
    ordered_list = sorted(zip(heights, infronts))
    heights = [x for x,y in ordered_list]
    infronts  = [y for x,y in ordered_list]

    result = [None for x in range(size)]

    for i in xrange(0, size):
        pos = find_empty_index(infronts[i], empty_index_list)
        result[pos] = heights[i]

    return result

A = [5, 3, 2, 6, 1, 4]
B = [0, 1, 2, 0, 3, 2]
print restore_the_line_3(A, B)
    
# A = [ 86, 77 ]
# B = [ 0, 1 ]
# print order(A, B)
            