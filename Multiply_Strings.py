class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]

        size = len(num1) + len(num2)
        d = [0 for i in range(size)]

        for i in xrange(0, len(num1)):
            a = int(num1[i])

            for j in xrange(0, len(num2)):
                b = int(num2[j])
                d[i + j] += a*b

        res = ''

        for i in xrange(0, size):
            digit = d[i]%10
            carry = d[i]/10
            res = str(digit) + res

            if i<size-1:
                d[i + 1] += carry

        # trim starting zeros
        while len(res)>0 and res[0]=='0':
            res = res[1:]

        return ('0' if len(res)==0 else res)

sol = Solution()
print sol.multiply("111","11")