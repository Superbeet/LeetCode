# -*- coding: utf-8 -*- 

"""
若p中当前char是'*'，则需要考虑其与之前一个char构成的组合能match多少个s中的char。对于向我这样的DP新手，这里有另一个思维方式需要去学习，就是要以“当前的数组元素应该得什么值”为思考的出发点，而不要去考虑整个问题，否则思路容易混乱，一个时刻只考虑眼下要解决的问题，而眼前的问题是只要这个组合能match上s中0/1/多个char组合这三种情况中的任意一种情况，就应该认为当前match数组元素要取true。

用来刻画这个组合match 0个char时的条件是p前一个char能不能match上s当前char，若能，说明当前p中的组合即使match 0个s中的char，依然可以认为s.substring(i)与p.substring(j)相match；

用来刻画这个组合match s中的1个char时的条件是p中'*'前面的char与s中的当前char相match；

用来刻画这个组合match s中的2个及以上char的条件是最难准确想到的：
首先当前p中的这个组合要能够满足p.substring(j) matches s.substring(i - 1)，也就是说这里要求这个组合至少要match两个s中的char，如果不能满足p.substring(j) matches s.substring(i - 1)，那么当前p中我们在考虑到这个组合至多能match一个s中的char。在满足了这第一个条件之后，这个组合同时还要再满足其代表的char能够match当前的s中我们在考虑的char，所以是match[i - 1][j] && isSame(s.charAt(i - 1), p.charAt(j - 2))。


s[i] =   b		 ba		baa
p[j] = ba*		ba*		ba*

"""

class Solution(object):
    def isMatch(self, s, p):
        match = [[False for x in range(len(p)+1)] for x in range(len(s)+1)] 
        # print match
        match[0][0] = True
        
        for i in xrange(0, len(s)+1):
            for j in xrange(1, len(p)+1):

                if i!=0:

                    if j>1 and p[j-1] == '*':
                        match[i][j] = match[i][j-2] or match[i][j-1] or (match[i-1][j] and self.isSame(s[i-1], p[j-2]))

                    elif match[i-1][j-1] and self.isSame(s[i-1], p[j-1]):
                        match[i][j] = True
                
                # if i == 0
                elif j>=2 and p[j-1]=='*' and match[0][j-2]:
                    match[0][j] = True

        # print match
        return match[len(s)][len(p)]

    def isSame(self, s, p):
        if p == '.' or s == p:
            return True
            
        return False

sol = Solution()
from time import clock
start = clock()
sol = Solution()
result = sol.isMatch("aa","a")
finish = clock()
print "%s(s)" %(finish-start)
print result




