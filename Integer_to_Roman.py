# 1, 2-3, 4,5,6-8,9
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""

        for i in xrange(0, 13):
        	if num>=nums[i]:
        		count = num/nums[i]
        		num %= nums[i]

        		for j in xrange(0, count):
        			res += "%s"%(romans[i])

        return res
