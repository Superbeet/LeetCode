"""
Given a sorted dictionary of an alien language, find order of characters
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
"""

def print_map(hashmap):
	for k,v in hashmap.iteritems():
		print "%s -> %s" %(k, v)

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = ""
        size = len(words)

        if size == 0:
            return ""

        graph = {}

        for i in xrange(0, size):
            for j in xrange(0, len(words[i])):
                c = words[i][j]
                if c not in graph:
                    graph[c] = set([])

                if i>0:
                    self.check(words[i-1], words[i], graph)
        # print_map(graph)
        stack = []
        visited = {}
        isloop = {}

        for c in graph.keys():
            if not self.topological_sort(graph, c , visited, isloop, stack):
                return ""

        print stack

        while len(stack):
            res += stack.pop(-1)

        return res

    def topological_sort(self, graph, c, visited, isloop, stack):
        if c in visited:
            return True

        if c in isloop:
            return False

        isloop[c] = True

        for next in graph[c]:
            if not self.topological_sort(graph, next, visited, isloop, stack):
                return False

        visited[c] = True

        stack.append(c)

        return True

    def check(self, word1, word2, hashmap):
        i = 0
        while i<len(word1) and i<len(word2):
            if word1[i]!=word2[i]:
                break
            i += 1

        if i<len(word1) and i<len(word2):
            hashmap[word1[i]].add(word2[i])

sol = Solution()
words = ["wrt","wrf","er","ett","rftt"]
words = ["x", "z"]
print sol.alienOrder(words)