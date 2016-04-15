"""
0 1 2 3 n
1 0 0 0 0
2 0 0 0 0
3 0 0 0 0 
m 0 0 0 0
"""

class UnionFind(object):
    def __init__(self, size):
        self.size = size
        self.ids = [-1]*size
        self.cnt = 0
        self.weight = [1]*size

    def find(self, i):
        while i!=self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]

        return i

    def union(self, m, n):

        i = self.find(m)
        j = self.find(n)

        if i!=j:
            if self.weight[i]<self.weight[j]:
                self.ids[i] = j
                self.weight[j]+=self.weight[i]
            else:
                self.ids[j] = i
                self.weight[i]+=self.weight[j]
            # can be improved
            # self.ids[i] = j 
            self.cnt -= 1

    def set_id(self, i):
        return self.ids[i]

    def add(self, i):
        if self.ids[i]==-1:
            self.ids[i] = i
            self.cnt += 1
            return True
        else:
            return False

    def count(self):
        return self.cnt

    def printf(self, n):
        for i in xrange(0, self.size):
            if i%n == 0:
                group = i/n
                row = ""
                for i in self.ids[group*n:(group+1)*n]:
                    row += "%3s " %str(i)
                print row

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        union_find = UnionFind(m*n)

        res = []

        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in xrange(0, len(positions)):
            y = positions[i][0]
            x = positions[i][1]
            index = y*n + x

            if union_find.add(index):
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    adj_index = ny*n+nx

                    if 0<=nx<n and 0<=ny<m and 
                      union_find.set_id(adj_index)!=-1:
                        root = union_find.union(index, adj_index)

            res.append(union_find.count())

        return res


sol = Solution()

# m = 3
# n = 3
# pos = [[0,0],[0,1],[1,2],[2,1]]

# m = 8
# n = 2
# pos = [[7,0]]

# m = 1
# n = 2
# pos = [[0,1],[0,0]]

m = 9
n = 9
pos = [[8,5],[8,0],[3,4],[0,3],[1,0],[5,4],[0,8],[5,7],[0,6],[6,2],[4,7],[2,7],[8,7],[8,6],[5,3],[2,3],[3,5],[3,1],[0,2],[8,8],[6,4],[0,1],[0,4],[7,5],[3,0]]

print sol.numIslands2(m, n, pos)
