"""
( ) parenthesis or round brackets 圆括号
[ ] square brackets 方括号
<> Angle brackets 尖括号
{} curly brackets or braces 大括号
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c == '(' or c == '[' or c=='{':
                stack.append(c)

            else:
                if not stack:
                    return False

                top = stack.pop()
                
                if c == ')':
                    if top!='(':
                        return False

                if c== ']':
                    if top!='[':
                        return False

                if c == '}':
                    if top!='{':
                        return False

        return not stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = [('A', 'a'), ('[', ']'), ('(', ')')]

        hashmap = {}
        for left, right in pairs:
            hashmap[left] = right

        stack = []

        for c in s:
            if c in hashmap.keys():
                stack.append(c)

            else:
                if not stack:
                    return False

                top = stack.pop()
                
                if c in hashmap.values():
                    if hashmap[top] != c:
                        return False

        return not stack

sol = Solution()
print sol.isValid("")
print sol.isValid("(")
print sol.isValid("(A[]a)")
print sol.isValid("A[(]a)")
print sol.isValid("A[]a")
print sol.isValid("aA[]")