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