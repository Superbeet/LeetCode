class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def peek(self):
        return self.stack[-1] 

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack)==0

    def __str__(self):
    	return "%s" %self.stack

    def __repr__(self):
    	return "%s" %self.stack

"""
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
        stk = stack()

        for c in s:
            if c == '(' or c == '[' or c=='{':
                stk.push(c)

            else:
                if stk.isEmpty():
                    return False

                top = stk.pop()
                print top
                if c==')':
                    if top!='(':
                    	return False

                if c==']':
                    if top!='[':
                    	return False

                if c=='}':
                    if top!='{':
                    	return False

        return stk.isEmpty()

sol=Solution()
print sol.isValid("()[]{}")
