class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        
        words = filter(None, words)

        size = len(words)

        new_words = []

        for i in xrange(size-1, -1, -1):
        	new_words.append(words[i])

        new_str = " ".join(new_words)

        return new_str