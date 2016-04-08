# Single call
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n==0:
            return n
        buffer = [None]*4
        count = 0
        i = 0
        while i<n:
            amount = read4(buffer)
            j = 0
            while j<amount and i<n:
                buf[i] = buffer[j]
                i += 1
                j += 1
            if amount!=4:
                break
            
        return i

# Multiply calls
class Solution(object):
    def __init__(self):
        self.start = 0
        self.end = 0
        self.buffer = [None]*4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buffer = self.buffer
        i = 0
        while i<n:
            if self.start == self.end:
                self.end = read4(buffer)
                self.start = 0
            
            while i<n and self.start<self.end:
                buf[i] = buffer[self.start]
                i += 1
                self.start += 1
            
            if self.end!=4:
                break
        return i