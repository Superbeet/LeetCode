import copy

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        half_strs, odd_char = self.has_permutation(s)
        if half_strs == None:
            return []
        
        half_strs = sorted(half_strs)
        visited = [False for i in xrange(len(half_strs))]
        self.res = []
        self.generate_permutations(half_strs, 0, odd_char, visited, "") 
        return self.res
        
    def has_permutation(self, s):
        def is_even(num):
            return num%2==0
        
        hashmap = {}
        
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        half_strs = []
        has_odd, odd_char = False, ""
        for char,freq in hashmap.iteritems():
            if not is_even(freq):
                if has_odd:
                    return None, ""
                else:
                    odd_char = char
                    has_odd = True
            half_strs += char*(hashmap[char]/2)
            
        return half_strs, odd_char
        
    def generate_permutations(self, s, start, odd_char, visited, string):
        if start == len(s):
            self.res.append(string+odd_char+string[::-1])
            return
        
        for i in xrange(0, len(s)):
            if not visited[i]:
                if i>0 and s[i]==s[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                self.generate_permutations(s, start+1, odd_char, copy.deepcopy(visited), string += s[i])
                visited[i] = False

sol = Solution()
print sol.generatePalindromes("zxcvbnmnbvcxz")