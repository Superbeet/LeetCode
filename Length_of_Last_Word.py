# Forward
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = 0
        cur_len = 0
        last_len = 0

        for c in s:

            if c!=" ":
                cur_len += 1

            elif cur_len!=0:
                last_len = cur_len
                cur_len = 0

        if cur_len!=0:
            last_len = cur_len

        return last_len