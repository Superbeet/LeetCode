"""Number of Connected Components in an Undirected Graph [Medium]

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges."""
class UnionFind(object):

    def __init__(self, size):
        self.ids = [None] * size

        for i in xrange(0, len(self.ids)):
            self.ids[i] = i

        self.cnt = size

    def find(self, m):
        return self.ids[m]

    def connected(self, m, n):
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

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if len(edges) == 0:
          return n

        groups = range(0, n)
        uf = UnionFind(n)

        for pair in edges:
            uf.union(pair[0], pair[1])

        return uf.count()

