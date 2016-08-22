"""
BFS
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n <= 1:
            return True
        
        if not edges:
            return False
                
        self.graph = {}
        for node, neigh in edges:
            if node not in self.graph:
                self.graph[node] = set([neigh])
            else:
                self.graph[node].add(neigh)
            
            if neigh not in self.graph:
                self.graph[neigh] = set([node])
            else:
                self.graph[neigh].add(node)
        # BFS check if there is a cycle
        import collections
        queue = collections.deque([])
        start_node = edges[0][0]
        queue.append(start_node)
        visited = set([start_node])    
        while queue:
            node = queue.popleft()
            for neigh in self.graph[node]:
                if neigh in visited:
                    return False
                visited.add(neigh)
                queue.append(neigh)
                #remove node from its neighbour's adjacent list
                self.graph[neigh].remove(node) 
        # Check if the whole graph is connected
        if len(visited) != n:
            return False
        
        return True

"""
Union-find set
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)

        for i in xrange(0, len(edges)):
            if not uf.union(edges[i][0], edges[i][1]):
                return False
        
        return uf.count() == 1

class UnionFind(object):

    def __init__(self, size):
        self.ids = [None] * size

        for i in xrange(0, len(self.ids)):
            self.ids[i] = i

        self.cnt = size

    def find(self, m):
        return self.ids[m]

    def are_connected(self, m, n):
        return self.find(m) == self.find(n)

    def count(self):
        return self.cnt

    def union(self, m, n):
        src = self.find(m)
        dst = self.find(n)
        # m, n not in same set yet
        if src!=dst:
            for i in xrange(0, len(self.ids)):
                if self.ids[i] == src:
                    self.ids[i] = dst

            self.cnt -= 1
            
            return True
        # m,n already in same set
        else:
        	# Find a loop
            return False
