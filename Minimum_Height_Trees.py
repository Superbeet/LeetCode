# 116, remove outdegree 0 nodes one by one until every node only has one adjcent node
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        adj_list = [set() for j in range(n)]
        # store the tree
        for s, e in edges:
            adj_list[s].add(e)
            adj_list[e].add(s)

        leaves = [i for i in range(n) if len(adj_list[i])<=1]

        while n>2:
            n -= len(leaves)
            new_leaves = []
            for x in leaves:
                for y in adj_list[x]:
                    adj_list[y].remove(x)
                    # calculate outdegrees
                    if len(adj_list[y])==1:
                        new_leaves.append(y)

            leaves = new_leaves

        return leaves

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n==1:
            return [0]

        res = []
        indegree = [0 for i in range(n)]
        adj_list = [set() for i in range(n)]
        queue = []

        for x,y in edges:
            adj_list[x].add(y)
            indegree[y] += 1
            adj_list[y].add(x)
            indegree[x] += 1

        for i in xrange(n):
            if indegree[i]==1:
                queue.append(i)

        while n>2:
            size = len(queue)

            for j in xrange(0, size):
                node = queue.pop(0)
                n -= 1
                
                for i in adj_list[node]:
                    indegree[i] -= 1

                    if indegree[i]==1:
                        queue.append(i)

        return queue
