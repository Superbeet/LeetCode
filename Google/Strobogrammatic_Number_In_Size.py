import copy
class Solution(object):
    def findAllStrobogrammatic(self, n):

        self.pair = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6",
        }
        
        self.digits = ["0", "1", "6", "8", "9"]

        res = []
        # for odd
        self.get_strobogrammatic(n, 1, ["0", "1", "8"], res)
        # for even
        self.get_strobogrammatic(n, 0, [""], res)

        return res

    def get_strobogrammatic(self, n, start, prev_group, res):
    	res.extend(copy.deepcopy(prev_group))

        for step in xrange(start, n, 2):
            str_group = []
            for string in prev_group:
                for key,val in self.pair.iteritems():
                    new_string = key+string+val
                    str_group.append(new_string)
                    if key != "0":
                        res.append(new_string)

            prev_group = str_group

sol = Solution()
print sorted(sol.findAllStrobogrammatic(5))