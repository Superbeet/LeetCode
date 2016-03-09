class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def check_alphanumeric(char):
            check =  char.isalpha() or char.isdigit()
            return check

        if not s:
            return True

        size = len(s)
        left = 0
        right = size-1

        while left<right:
            
            while left<size and not check_alphanumeric(s[left]):
                left += 1

            while right>=0 and not check_alphanumeric(s[right]):
                right -= 1

            if left>=right:
                return True

            if s[left].lower()!=s[right].lower():
                return False

            left += 1
            right -= 1

        return True
        