# time - O(2^n)
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.res = []
        
        self.generate(0, word, "", 0)
        
        return self.res

    def generate(self, start, word, string, count):
        size = len(word)
        str_size = len(string)
        
        if start == size:
            if count>0:
                string += str(count)
            self.res.append(string)
        
        else:
            self.generate(start+1, word, string, count+1)
            
            if count>0:
                string += str(count)
            string += word[start]
            self.generate(start+1, word, string, 0)
        
        string = string[:str_size+1]
        
sol = Solution()
print sol.generateAbbreviations("abc")
# print sol.postfix_num("abc1")
# print sol.postfix_num("abc12")
# print sol.postfix_num("abc123")
# print sol.postfix_num("abc1234")