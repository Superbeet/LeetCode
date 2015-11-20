## 64 ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b

        if not b:
            return a

        if len(a)>len(b):
            return self.addBinary(b, a)
        
        carry = 0
        digit = 0
        binary_sum = ""
        dig_sum = 0
        
        for i in range(1, len(a)+1):
            dig_sum = int(a[-i])+int(b[-i])+carry
            carry = dig_sum/2
            digit = dig_sum%2
            binary_sum = str(digit)+binary_sum
        
        for j in range(len(a)+1, len(b)+1):
            dig_sum = int(b[-j])+carry
            carry = dig_sum/2
            digit = dig_sum%2
            binary_sum = str(digit)+binary_sum
        
        if carry!=0:
            binary_sum = str(carry)+binary_sum

        return binary_sum
##72 ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b

        if not b:
            return a

        if len(a)>len(b):
            self.addBinary(b, a)

        carry = 0
        digit = 0
        binary_sum = ""

        i = len(a)-1
        j = len(b)-1

        while i>=0 or j>=0:

        	addend_1 = int(a[i]) if i>=0 else 0
        	addend_2 = int(b[j]) if j>=0 else 0

        	digit_sum = addend_1 + addend_2 + carry
        	carry = digit_sum/2
        	digit = digit_sum%2

        	binary_sum += str(digit)

        	i-=1
        	j-=1

        return binary_sum[::-1]
