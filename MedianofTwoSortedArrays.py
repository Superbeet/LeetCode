class Solution:
	# 首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。
	# 用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
	# 如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，
	# 而A中的第3个数A[2]=5；B中的第3个数B[2]=6；而A[2]<B[2]；则A[0]，A[1]，A[2]中
	# 必然不可能有第7个小的数。因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1]
	# 这四个数，也就是说A[2]最多可能是第5个大的数，由于我们要求的是getKth(A, B, 7)；
	# 现在就变成了求getKth(A', B, 4)；即A' = {7}；B不变，求这两个数列的第4个小的数，
	# 因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB: 
        	return self.getKth(B, A, k)
        if lenA == 0: 
        	return B[k - 1]
        if k == 1: 
        	return min(A[0], B[0])
        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + \
             		self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5