class Solution(object):
    def getPermutation(self, n, k):
        facs = [1]
        nums = []
        for j in xrange(1, n):
            facs.append(facs[-1]*j)
        
        for i in range(1, n + 1):
            nums.append(i)
        
        per = []
        
        res = []
        
        remain = k - 1
        
        for i in xrange(n):
            fac = facs[n-1-i]
            index = remain / fac
            remain = remain % fac
            res.append(str(nums[index]))
            nums.pop(index)
        
        return "".join(res)
            
            