import re

class InputError(Exception):
    pass

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        
        output = ""

        for s in strs:
            if not isinstance(s, basestring):
                raise InputError("Non-string input is found")
                break

            output += str(len(s)) + '#'
            output += str(s)

        return output

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        idx = 0
        res = []
        start = 0

        while start < len(s):
            idx = s.index('#', start)
            # size = int(s[idx-1])
            # print start, idx
            obj = re.search(r'\d+', s[start:idx])
            size = int(obj.string)
            res.append(s[idx+1:idx+1+size])

            start = idx+1+size

        return res

# Your Codec object will be instantiated and called as such:
strs = [
    "Hello",
    "World",
    "Encodes a list of strings to a single string."
]

codec = Codec()
tmp = codec.encode(strs)
print tmp
print codec.decode(tmp)