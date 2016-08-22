class UnionFind(object):
    def __init__(self, size):
        self.size = size
        self.ids = [-1]*size
        self.cnt = 0
        # self.weight = [1]*size

    def find(self, i):
        while i!=self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]

        return i

    def union(self, m, n):

        i = self.find(m)
        j = self.find(n)

        if i!=j:
            # if self.weight[i]<self.weight[j]:
            #     self.ids[i] = j
            #     # self.weight[j]+=self.weight[i]
            # else:
                # self.ids[j] = i
                # self.weight[i]+=self.weight[j]
            # can be improved
            self.ids[i] = j 
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
