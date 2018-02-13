class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        def sorted(s):
            return "".join(sorted(s))
        
        hashmap = {}
        
        for string in strs:
            sorted_str = sorted(string)
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [string]
            else:
                hashmap[sorted_str].append(string)
        
        result = []
        for value in hashmap.values():
            result.extend(value)
        
        return result

sol = Solution()
sol.anagrams(["lint","intl","inlt","code"])