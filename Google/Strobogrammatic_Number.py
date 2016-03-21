class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def is_equal(digit1, digit2):
            if digit1=="6":
                return digit2=="9"
            
            if digit1=="9":
                return digit2=="6"
            
            if digit1 in ["0","1","8"]:
                return digit2==digit1
            
            return False
            
        string = str(num)
        size = len(string)
        i, j = 0, size-1
        # No need to seperate odd and even case, any digit equals to itself
        while i<=j:
            if not is_equal(string[i], string[j]):
                return False            
            i += 1
            j -= 1
        
        return True