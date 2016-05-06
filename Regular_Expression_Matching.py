# -*- coding: utf-8 -*
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
class Solution1:
    def isEqual(self, s0, p0):
        if s0 == p0 or p0=='.':
            return True
        else:
            return False
        
    def isMatch(self, s, p):
        if len(p)==0: 
            return len(s)==0
        
        if len(p)==1 or p[1] != '*':
            if len(s) and self.isEqual(s[0], p[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        
        else:
            if len(s) and self.isEqual(s[0], p[0]):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:],p)
            else:
                return self.isMatch(s, p[2:])

class Solution2:
    def is_same(self, s, p):
        if s[0]==p[0] or p[0]==".":
            return True
        return False

    def isMatch(self, s, p):

        if len(p)==0:  
            return len(s)==0

        if len(p)==1 or p[1]!='*':
            if len(s)==0:
                return False

            if self.is_same(s[0], p[0]):
                return False
                
            return self.isMatch(s[1:], p[1:])
            
        i =- 1
        length = len(s)

        while i<length and (i==-1 or p[0]=='.' or p[0]==s[i]):
            if self.isMatch(s[i+1:], p[2:]):                 
                return True
                
            i+=1
            
        return False

sol = Solution1()
print sol.isMatch("aa","a") # false
print sol.isMatch("aaa","aa") # false
print sol.isMatch("aa","aa") # true
print sol.isMatch("aa", "a*") # true
print sol.isMatch("aa", ".*") # true
print sol.isMatch("ab", ".*") # true
print sol.isMatch("aab", "c*a*b") # true
print sol.isMatch("abc","a*a*a*a*a*bc")
print sol.isMatch("aa","a.")
print sol.isMatch("ab",".*c")