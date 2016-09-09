# DP O(MN)
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        len1 = len(word1)
        len2 = len(word2)
        f = [[0] * (len2 + 1) for i in range(len1 + 1)] 
        for i in range(len1 + 1):
            f[i][0] = i
        for j in range(len2 + 1):
            f[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word2[j - 1] == word1[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
                        
        return f[len1][len2]

# Recursion Bruteforce O(2^(M+N))
class Solution:
    def minDistance(self, word1, word2):
        if len(s) == 0:
            return len(t)

        if len(t) == 0:
            return len(s)

        delete = self.minDistance(word1[:-1], word2) + 1
        insert = self.minDistance(word1, word2[:-1]) + 1
        if word1[-1] == word2[-1]:
            replace = self.minDistance(word1[:-1], word2[:-1]) 
        else:
            replace = self.minDistance(word1[:-1], word2[:-1]) + 1

        return min(delete, insert, replace)


# Overtime
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)>len(word2):
           return self.get_min_distance(word2, word1)
       
        else:
           return self.get_min_distance(word1, word2)

    def get_min_distance(self, word1, word2):

        if word1=="":
            return len(word2)

        # shift = 0
        diff = 0
        i = 0
        j = 0

        while i<len(word1) or j<len(word2):

            print "i->", i
            print "j->", j 

            letter_1 = (word1[i] if i<len(word1) else "")
            letter_2 = (word2[j] if j<len(word2) else "")

            if letter_1!=letter_2:
                diff += 1

                if len(word2)-diff+1!=len(word1):
                    i -= 1

            i += 1
            j += 1

        return diff

import unittest

class TestSolution(unittest.TestCase):
    """docstring for TestSolution"""
    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        pass

    def test_min_distance(self):
        print "min_distance"
        self.assertEquals(self.sol.minDistance("a","b"), 1)
        self.assertEquals(self.sol.minDistance("ab","bc"), 1)

if __name__ == '__main__':
    unittest.main()