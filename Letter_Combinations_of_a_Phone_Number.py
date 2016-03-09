class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.mapping = [
            [],
            [],
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z'],
        ]

        self.res = []
        
        if digits == "":
            return self.res

        size = len(digits)

        self.buildCombinations(digits, size, "", 0)

        return self.res

    def buildCombinations(self, digits, size, cur_str, cur_idx):

        if cur_idx > size-1:
            self.res.append(cur_str)
            return

        num = int(digits[cur_idx])

        for i in xrange(0, len(self.mapping[num])):
            cur_str += self.mapping[num][i]
            self.buildCombinations(digits, size, cur_str, cur_idx+1)
            cur_str = cur_str[0:-1]

        return

sol = Solution()
print sol.letterCombinations("9")



