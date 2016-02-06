class UnionFind(object):

    def __init__(self, size):
        self.ids = range(size)
        self.cnt = size
        
    def count(self):
        return self.cnt

    def union(self, m, n):
    	print "m,n -> %s,%s" %(m, n)
        i = self.root(m)
        j = self.root(n)

        print "i,j -> %s,%s" %(i, j)
        
        if i!=j:
            self.ids[i] = j
            self.cnt -= 1
            print self.ids
            print ""
            return True
        # m,n already in same set
        else:
            # Find a loop
            return False

    def find(self, m):
        return self.ids[m]

    def connected(self, m, n):
        return self.find(m) == self.find(n)

    def root(self, i):

        while i!=self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]

        return i

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)

        for pair in edges:
            union_find.union(pair[0], pair[1])

        return union_find.count()

sol = Solution()

edges = [
    [2,1],[2,3],[4,5]
]

print sol.countComponents(6, edges)