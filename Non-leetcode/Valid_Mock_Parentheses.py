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