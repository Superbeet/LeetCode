class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        common = ""
        new_char = ""

        if not strs:
            return common

        while 1:
            
            for n in range(0, len(strs)):
                if n==0 and i<len(strs[0]):
                    new_char = strs[0][i]

                if i >= len(strs[n]) or new_char!=strs[n][i]:
                    return common                
            
            common += new_char

            i += 1

        return common
