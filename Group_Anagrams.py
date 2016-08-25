class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
            
        hashmap = {}
        for string in strs:
            # sorted_str = "".join(sorted(string)) # Solution 1 - sorted
            str_counter = self.char_counter(string) # Solution 2 - asc counter
            if str_counter not in hashmap:
                hashmap[str_counter] = [string]
            else:
                hashmap[str_counter].append(string)

        result = []
        for strings in hashmap.values():
            result.append(strings)
        return result
        
    def char_counter(self, string):
        counter = [0 for i in range(26)]
        for c in string:
            counter[ord(c)-ord("a")] += 1
        return str(counter)        