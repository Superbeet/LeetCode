class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.res = []

        length = len(s)

        if length>12 or length<4:
            return self.res

        self.calcu_ip(s, 0, [])

        return self.res

    def calcu_ip(self, s, idx, ip_nums):
        
        if len(ip_nums)==4:
            if idx == len(s):

                ip_digit = ".".join(ip_nums)

                self.res.append(ip_digit)

            return

        cur_num = ""
        j = idx

        while j<len(s) and j<idx+3:
            cur_num += s[j]

            if self.is_valid_num(cur_num):
                ip_nums.append(cur_num)
                self.calcu_ip(s, j+1, ip_nums)
                ip_nums.pop(-1)

            j += 1

    def is_valid_num(self, s):
        if s == "" or len(s)>3:
            return False

        if s[0]=='0' and len(s)!=1:
            return False

        if len(s)==3 and int(s)>255:
            return False

        return True



        # if idx > len(s)-1:
        #     return


        # for size in xrange(1, 4):
        #     if size <= len(s)-1-idx:

        #         prev_str = ip_nums

        #         if count <= 3:
        #             ip_nums += s[idx:(idx+size)] + "."
        #         else:
        #             ip_nums += s[idx:(idx+size)]

        #         self.calcu_ip(s, idx+size, ip_nums, count+1)

        #         ip_nums = prev_str

        # if count == 4:
        #     if len(s)-1-idx==0:
        #         self.res.append(ip_nums)
        #     return 

        # return

sol = Solution()
sol.restoreIpAddresses("2552552551")
print sol.res
