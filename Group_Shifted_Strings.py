# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# Return:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

import string
import copy

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        res = []
        hashmap = {}

        for i in xrange(0, len(strings)):

            if i not in hashmap:
                group = []
                group.append(strings[i])
                hashmap[i] = True

                for j in xrange(i+1, len(strings)):

                    if j not in hashmap:

                        if self.check_group(strings[i], strings[j]):
                            group.append(strings[j])
                            hashmap[j] = True

                res.append(sorted(group))

        return res

    def check_group(self, string_1, string_2):
        if len(string_1) != len(string_2):
            return False

        letters = string.ascii_lowercase
        letters_size = len(letters)
        start = string_1[0]
        start_pos = letters.index(start)
        # new_str = ""
        shift = 0

        while 1:

            new_str = ""

            for j in xrange(0, len(string_1)):

                pos = letters.index(string_1[j])
                
                real_pos = pos+shift
                # round up letter pos if reach the maximun
                if real_pos > letters_size-1:
                    real_pos = real_pos - letters_size

                new_str += letters[real_pos]

            if new_str == string_2:
                return True


            if shift == letters_size:
                return False
            
            shift += 1

        return False



        # start_pos = letters.index(start)
        # end_pos = letters.index(start)
        # cur_pos = start_pos

        # while 1:

        #     if string_1 == string_2:
        #         return True

        #     string_1 = string_1[1:] + letters[cur_pos+1]

        #     cur_pos += 1

        #     if cur_pos == len(letters)-1:
        #         cur_pos = 0

        #     if cur_pos == start_pos:
        #         return False

        # return False


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