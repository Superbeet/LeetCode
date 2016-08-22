# 2nd Time
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        key_map = {
            1:[],
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"],
            0:[]
        }
        
        result = []
        self.get_combination(key_map, digits, 0, [], result)
        return result
        
    def get_combination(self, key_map, digits, start, ans, result):
        if start == len(digits):
            result.append("".join(ans))
            return

        num = int(digits[start])
        for letter in key_map[num]:
            ans.append(letter)
            self.get_combination(key_map, digits, start+1, ans, result)
            ans.pop()
        
# 1st Time
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



