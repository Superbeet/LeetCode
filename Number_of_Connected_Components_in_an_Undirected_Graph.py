class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # initial
        ids = range(0, n)

        print ids

        for pair in edges:
            i = root(pair[0])
            j = root(pair[1])
            ids[i] = j
            # ids[i] = ids[j]
        print ids

        count = 0

        id_set = set(ids)

        return len(id_set)

    def root(self, ids, i):
        
        while i!=ids[i]:
            ids[i] = ids[ids[i]]
            i = ids[i]

        return i

sol = Solution()
edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
sol.countComponents(6, edges)