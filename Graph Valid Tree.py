class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # initial
        ids = range(0, n)

        for pair in edges:
            i = ids[pair[0]]
            j = ids[pair[1]]
            
            if i!=j:
                ids[i] = j
            # ids[i] = ids[j]

        count = 0

        id_set = set(ids)
        print id_set
        return len(id_set)

    # def root(ids, i):
        
    #     while i!=ids[i]:
    #         ids[i] = ids[ids[i]]
    #         i = ids[i]

    #     return i

sol = Solution()
edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
sol.validTree(edges)