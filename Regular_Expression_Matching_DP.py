"""Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

s-index->i
s-index->j
1. 正常字符，即不是'*'也不是'.'
这种比较好处理，只要两个字符串向前一位能够匹配的同时两字符串最后一个字符相等, 可得到 

dp[i][j] = dp[i - 1][j - 1] && s.charAt(i - 1) == p.charAt(j - 1)

2. 字符为'.'
这种相对也比较好处理，只要两个字符串向前一位能够匹配即可，因为'.'能匹配字符串s的任意字符，所以可得到

dp[i][j] = dp[i - 1][j - 1]

3. 字符为'*'
这种比较复杂，因为'*'能匹配任意个数的前面的字符。
所以我们可以先考虑能够匹配0个和1个前面字符的简单情况，比如

匹配1个表示取0个前面字符意味着忽略自己，可到
dp[i][j] = dp[i][j - 1];

匹配0个表示可以忽略自己及前面那个字符，可得
dp[i][j] = dp[i][j - 2];

再考虑匹配2个及2个以上前面字符的情况，这种情况可以这么考虑:
如果dp[i][j] = true是'*'匹配k(k>=2)个前面字符的结果，那么'*'匹配k-1个前面字符的结果也必须是true，所以条件之一便是dp[i - 1][j] == true，另外一个条件便是s的最后一个字符必须匹配p的'*'前面的字符，所以得到
dp[i][j] = dp[i -1][j] && (p.charAt(j - 2) == s.charAt(i - 1) || p.charAt(j - 2) == '.'

"""


# 92ms Dynamic Programming
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        #i=0
        for j in xrange(0, len(p)+1):
            if j>1 and p[j-1]=='*':
                dp[0][j] = dp[0][j-1] or dp[0][j-2]

        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):

                if p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]

                elif p[j-1]=='*':

                    if dp[i][j-2]:
                        dp[i][j] = True
                    
                    elif dp[i][j-1]:
                        dp[i][j] = True
                    
                    elif dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'):
                        dp[i][j] = True

                elif dp[i-1][j-1] and p[j-1]==s[i-1]:
                    dp[i][j] = True

        return dp[len(s)][len(p)]

