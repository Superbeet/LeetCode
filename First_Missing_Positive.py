class Solution(object):
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
            return 1
            
        size = len(A)
        
        i = 0
        while i < size:
            if A[i] != i + 1 and A[i] >= 1 and A[i] <= size and A[i] != A[A[i]-1]:
                t = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = t
            else:
                i += 1
        
        for j in xrange(1, size + 1):
            if A[j-1] != j:
                return j

        return size + 1
        
sol = Solution()
assert sol.firstMissingPositive([-1, 1, 3, 4]) == 2
assert sol.firstMissingPositive([1,2,0]) == 3
assert sol.firstMissingPositive([3,4,-1,1]) == 2