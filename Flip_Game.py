class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        size = len(s)

        for i in range(0, size-1):
            if s[i] == '+' and s[i+1] == '+':
                s = s[:i] + "--" + s[i+2:]
                res.append(s)
                s = s[:i] + "++" + s[i+2:]

        return res