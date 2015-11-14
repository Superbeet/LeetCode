class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
        	return 0

        if n == 0:
        	return 1

        if n == 1:
        	return 1

        count = [None] * (n+1)
        count[0] = 1
        count[1] = 1

        for i in range(2, n+1):

            for j in range(0, i):

                count[i] += count[j]*count[i-j-1]

        return count[n]