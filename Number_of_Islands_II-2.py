class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.ids = [-1]*(m*n)
        self.size = [1]*(m*n)
        self.cnt = 0

        res = []

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        for y,x in positions:

            index = y*n+x

            if self.ids[index]==-1:
                self.ids[index] = index
                self.cnt += 1

                for dy, dx in dirs:
                    adj_y = y + dy
                    adj_x = x + dx
                    adj_index = adj_y*n+adj_x

                    if 0<=adj_x<n and 0<=adj_y<m and self.ids[adj_index]!=-1:
                        self.union(index, adj_index)

            res.append(self.cnt)

        return res

    def find(self, i):
        while i!=self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def union(self, m, n):
        i = self.find(m)
        j = self.find(n)

        if i!=j:
            if self.size[i]<self.size[j]:
                self.ids[i] = j
                self.size[j] += self.size[i]
            else:
                self.ids[j] = i
                self.size[i] += self.size[j]

            self.cnt -= 1


sol = Solution()

# m = 3
# n = 3
# pos = [[0,0],[0,1],[1,2],[2,1]]

# m = 8
# n = 2
# pos = [[7,0]]

m = 1
n = 2
pos = [[0,1],[0,0]]

# m = 9
# n = 9
# pos = [[8,5],[8,0],[3,4],[0,3],[1,0],[5,4],[0,8],[5,7],[0,6],[6,2],[4,7],[2,7],[8,7],[8,6],[5,3],[2,3],[3,5],[3,1],[0,2],[8,8],[6,4],[0,1],[0,4],[7,5],[3,0]]

print sol.numIslands2(m, n, pos)
