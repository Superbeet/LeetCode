class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        self.pair = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6",
        }
        
        self.digits = ["0", "1", "6", "8", "9"]
        
        res, ans = [], []
        mid = n/2
        
        if n==1:
            return ["0", "1", "8"]
        
        res = []
        
        if n%2==1:
            for digit in ["0", "1", "8"]:
                self.generate_postfix(n, 1, digit, res)
        else:
                self.generate_postfix(n, 0, "", res)
                
        return res
            
    def generate_postfix(self, n, count, string, res):
        
        if count == n:
            res.append(string)
            return
        
        if count >= n-2:
            for digit in self.digits[1:]:
                self.generate_postfix(n,count+2,digit+string+self.pair[digit],res)
        else:
            for digit in self.digits:
                self.generate_postfix(n,count+2,digit+string+self.pair[digit],res)
        
        return res
        
sol = Solution()
# print sol.findStrobogrammatic(2)
print sol.findStrobogrammatic(3)
        
    
        