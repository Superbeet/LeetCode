# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# Return:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        hashmap = {}

        for string in strings:
            key = ""
            start = string[0]
            shifts = []
            for c in string:
                shift = (ord(c) - ord(start))%26
                # key += "%02d"%(shift)
                shifts.append(shift)

            key = tuple(shifts)

            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)

        return map(sorted, hashmap.values())


import unittest

class TestGroup(unittest.TestCase):

    def test_init(self):
        sol = Solution()
        # sol.check_group("abc", "bcd")
  #       self.assertEquals(d.a, 1)
  #       self.assertEquals(d.b, 'test')
        self.assertTrue(sol.check_group("abc", "bcd"))
        self.assertTrue(sol.check_group("abc", "cde"))
        self.assertTrue(sol.check_group("cde", "abc"))
        self.assertTrue(sol.check_group("az", "ba"))

    def test_generate(self):
        sol = Solution()
        input_val = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        output_val = [
                          ["abc","bcd","xyz"],
                          ["az","ba"],
                          ["acef"],
                          ["a","z"]
                    ]

        self.assertEquals(sol.groupStrings(input_val), output_val)


# sol = Solution()
# sol.check_group("abc", "bcd")