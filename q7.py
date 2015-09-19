# Reverse Integer

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        result = 0

        if x == 0:
        	return 0

        if x < 0:
        	sign = -1
        else:
        	sign = 1

       	x = abs(x)

        while x>0:

        	digit = x%10

        	result = result*10 + digit

        	x = x/10

        if result>2**31 or result<0:
        	return 0

        return result*sign

if __name__ == '__main__':
	solution = Solution()
	
	test_list = [123, -123, 0, 100, 1534236469]
	
	for i in test_list:
	
		result = solution.reverse(i)
		
		print "input->%s, output->%s" %(i, result)
		


