class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rnd = 0
        seq = "1"

        if not n:
            return ""

        while rnd<n-1:

            seq = self.do_count_and_say(seq)
            # print "seq->", seq
            rnd += 1

        return seq

    def do_count_and_say(self, num_str):
        pre = 0
        cnt = 1
        res = ""
        m = len(num_str)-1

        for digit in num_str:

            if pre is not 0:

                if digit == pre:
                    cnt += 1
                else:
                    res = "%s%s" %(res, cnt) + pre
                    # print "res->", res
                    cnt = 1        	
            
            pre = digit

        res = "%s%s" %(res, cnt) + pre

        return res

sol = Solution()
# print sol.do_count_and_say("111122223333")
# print sol.do_count_and_say(0)
print sol.countAndSay(4)

