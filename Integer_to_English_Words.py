"""
      123 -> "One Hundred Twenty Three"
   12,345 -> "Twelve Thousand Three Hundred Forty Five"
1,234,567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

-2147483648 ~ 2147483647
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        v = ["Thousand", "Million", "Billion"]

        res = self.convertHundred(num % 1000)

        for i in xrange(0, 3):
            num /= 1000
            # print "res->", res
            # print "num->", num
            res = (self.convertHundred(num % 1000) + " " + v[i] + " " + res if num % 1000 else res)
            # res = num % 1000 ? convertHundred(num % 1000) + " " + v[i] + " " + res : res

        # print "<%s>"%res

        while len(res)>0 and res[-1] == ' ':
            res = res[:-1]

        return ("Zero" if len(res)==0 else res)

    def convertHundred(self, num):
        ones = ["", "One", "Two", "Three", "Four", 
                "Five", "Six", "Seven", "Eight", "Nine", 
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", 
                "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", 
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        res = ""
        a = num/100 # 3rd digit
        x = num%100 # 1st and 2nd digits
        b = x/10
        c = num%10  # 1st digit

        if x>0 and x<20:
        	res = ones[x]
        else:	# x>=20
        	if c:
        		res = tens[b]+" "+ones[c]
        	else:
        		res = tens[b]

        if a>0:
            res = ones[a] + " Hundred" + (" " + res if x else "")

        return res

sol = Solution()
# print sol.numberToWords(31400900)
print sol.numberToWords(50868)