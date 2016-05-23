class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [0 for x in range(n)]
        ways[0] = 1
        
        for i in xrange(0, m):
            for j in xrange(1, n):
                ways[j]= ways[j] + ways[j-1]
            print ways

        return ways[-1]

sol = Solution()
sol.uniquePaths(5, 5)