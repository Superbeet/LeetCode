class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path is "":
            return path

        path_elems = path.split("/")

        new_path_elems = []

        i = 0

        while i<len(path_elems):

            if path_elems[i] == ".":
            	pass

            elif path_elems[i] == "":
                pass

            elif path_elems[i] == "/":
            	pass

            elif path_elems[i] == "..":
            	if len(new_path_elems)!=0:
                	new_path_elems.pop(-1)

            else:
            	new_path_elems.append(path_elems[i])

            i += 1

        new_path = "/" + "/".join(new_path_elems)

        return new_path

import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        # self.widget = Widget("The widget")
        self.sol = Solution()

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        pass

    def testSimlifyPath(self):
        self.assertEqual(self.sol.simplifyPath("/home/"), "/home")
        self.assertEqual(self.sol.simplifyPath("/../"), "/")
        self.assertEqual(self.sol.simplifyPath("/../../../../"), "/")
        self.assertEqual(self.sol.simplifyPath("/a/./b/../../c/"), "/c")

    # def testDefaultSize(self):
    #     assert self.widget.size() == (50,50), 'incorrect default size'

if __name__ == '__main__':
    unittest.main()