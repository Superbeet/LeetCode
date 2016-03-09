class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)>len(t):
            return self.is_one_edit_distance(t, s)
        else:
            return self.is_one_edit_distance(s, t)

    def is_one_edit_distance(self, s, t):
        i = 0
        j = 0
        diff = 0

        while i<len(s) or j<len(t):

            char_1 = (s[i] if i<len(s) else "")
            char_2 = (t[j] if j<len(t) else "")

            if char_1!=char_2:
                
                if diff == 1:
                    return False

                diff = 1

                if len(s)!=len(t):
                    i -= 1

            i += 1
            j += 1

        if diff == 1:
            return True

        else:
            return False

import unittest

class testIsOneEditDistance(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        pass

    def test_one_distance(self):
        self.assertFalse(self.sol.isOneEditDistance("abc","abc"))
        self.assertTrue(self.sol.isOneEditDistance("abc","abcd"))
        self.assertTrue(self.sol.isOneEditDistance("abc","bbc"))

if __name__ == '__main__':
    unittest.main()

    # sol = Solution()
    # print sol.isOneEditDistance("abc","bbc")