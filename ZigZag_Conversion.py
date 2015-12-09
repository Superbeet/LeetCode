class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<2:
            return s

        ret = ""
        inc = (numRows-1)*2

        for i in range(0, numRows):
            j = i
            d1 = (numRows-i-1)*2
            # d2 = numRows-2-d1

            while j<len(s):
                ret += s[j]
                # 1st line and last line have no oblique numbers
                if d1!=0 and d1!=inc and j+d1<len(s):
                    ret += s[j+d1]

                j += inc

        return ret
