"""276. Paint Fence [Easy]
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts 
have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers."""

# class Solution(object):
#     def numWays(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: int
#         """
#         if n==0:
#             return 0

#         if n==1:
#             return k

#         if n==2:
#             return k*k

#         dp = [0 for i in range(n)]

#         dp[0] = k
#         dp[1] = k*k

#         for x in xrange(2, n):
#             dp[x] = (k-1)*(dp[x-1]+dp[x-2])
#             print dp

#         return dp[-1]

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0, k, k*k, 0]

        if n<=2:
            return dp[n]

        for x in xrange(2, n):
            dp[3] = (k-1)*(dp[2]+dp[1])
            dp[1] = dp[2]
            dp[2] = dp[3]
            # print dp
        return dp[3]

sol = Solution()
print sol.numWays(4, 2)
