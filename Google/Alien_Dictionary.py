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


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return
        
        graph = {}
        degrees = {}
        
        # Initialize graph and degree
        self.init_graph(words, graph, degrees)

        # Build graph and degree
        self.build_graph(words, graph, degrees)
        
        # print "graph  ->", graph
        # print "degrees->", degrees
        
        # Find starting zero indegree nodes
        from collections import deque
        queue = deque([])
        
        for node, indegree in degrees.iteritems():
            if indegree == 0:
                queue.append(node)
        
        # Start topological sort
        result = ""
        count = 0
        while queue:
            n = queue.popleft()
            count += 1
            result += n   
            if n in graph:
                for nb in graph[n]:
                    degrees[nb] -= 1
                    if degrees[nb] == 0:
                        queue.append(nb)
        
        if count == len(degrees):
            return result
        else:
            return ""
    
    def init_graph(self, words, graph, degree):
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
                if char not in degree:
                    degree[char] = 0
        return True
        
    def build_graph(self, words, graph, degree):
        
        visited = set()
        
        for i in xrange(1, len(words)):
            n, m = 0, 0
            
            while n < len(words[i-1]) and n < len(words[i]):
                prev = words[i-1][n]
                cur = words[i][n]
                
                if prev != cur:
                    if prev not in graph:
                        graph[prev] = set([cur])
                    else:
                        graph[prev].add(cur)
                    
                    pattern = prev + "_" + cur
                    
                    if pattern not in visited:
                        degree[cur] += 1
                        visited.add(pattern)
                        
                    break
                n += 1
            
        return True

sol = Solution()
words = ["wrt","wrf","er","ett","rftt"]
words = ["x", "z"]
print sol.alienOrder(words)