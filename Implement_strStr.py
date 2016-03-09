"""
Input:
haystack = 'aabbaa'; needle='bb'
Output:
return = 'bbaa'

预处理不需要按照P的定义写成O(m^2)甚至O(m^3)的。
我们可以通过P[1],P[2],…,P[j-1]的值来获得P[j]的值。
对于刚才的B="ababacb"，假如我们已经求出了P[1],P[2],P[3]和P[4]，
看看我们应该怎么求出P[5]和P[6]。P[4]=2，那么P [5]显然等于P[4]+1，
因为由P[4]可以知道，B[1,2]已经和B[3,4]相等了，现在又有B[3]=B[5]，
所以P[5]可以由P[4] 后面加一个字符得到。P[6]也等于P[5]+1吗？
显然不是，因为B[ P[5]+1 ]<>B[6]。那么，我们要考虑“退一步”了。
我们考虑P[6]是否有可能由P[5]的情况所包含的子串得到，即是否P[6]=P[ P[5] ]+1。
这里想不通的话可以仔细看一下：
"""
# 48 ms
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1
        
        m = len(haystack)
        n = len(needle)

        for i in xrange(0, m-n+1):
            for j in xrange(0, n):
                p1 = haystack[i+j]
                p2 = needle[j]

                if p1!=p2:
                    break

                if j == n-1:
                    return i

        return -1

# KMP Solution 84m
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1

        m = len(haystack)
        n = len(needle)
        match = self.kmp_process(needle)
        
        j = -1

        for i in xrange(0, m):
            while j>=0 and haystack[i]!=needle[j+1]:
                j = match[j]

            if haystack[i] == needle[j+1]:
                j +=1

            if j == n-1:
                return i-n+1
                
        return -1

    def kmp_process(self, s):
        n = len(s)
        match = [-1 for x in range(n)]

        j = -1

        for i in xrange(1, n):
            
            while j>=0 and s[i]!=s[j+1]:
                j = match[j]

            if s[i]==s[j+1]:
                j += 1

            match[i] = j

        return match
import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.sol = Solution2()

    # def tearDown(self):
    #     self.widget.dispose()
    #     self.widget = None

    def testFound(self):
        self.assertEqual(self.sol.strStr("abcde","cde"), 2)
        self.assertEqual(self.sol.strStr("abcde","bcd"), 1)
        self.assertEqual(self.sol.strStr("abcde","abc"), 0)

